class Bishop(Piece):
    def __init__(self, color, xPos, yPos):
        Piece.__init__(self, xPos, yPos, color)
        self.piecetype = 'bishop'

    # Return positions where we can move with or withour eating
    def get_move(self, game):

        yPos, xPos = self.yPos, self.xPos
        
        mapGame = game.map
        eat = []
        castling = []
        movement = []

        cases = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

        for e1, e2 in cases:
            di = [[yPos, xPos]]
            while 0 <= di[-1][0] + e1 < 8 and 0 <= di[-1][1] + e2 < 8 and mapGame[di[-1][0] + e1][di[-1][1] + e2] == 0:
                di += [[di[-1][0] + e1, di[-1][1] + e2]]
            if 0 <= di[-1][0] + e1 < 8 and 0 <= di[-1][1] + e2 < 8 and mapGame[di[-1][0] + e1][di[-1][1] + e2].color != self.color:
                eat += [[di[-1][0] + e1, di[-1][1] + e2]]
            movement += di[1:]

        return movement, eat, castling, []
