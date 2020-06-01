class Queen:
    def __init__(self, color):
        self.colors = color
        self.piecetype = 'queen'

    # Return position where can move
    def move(self, yPos, xPos, game):
        mapGame = game.map
        eat = []
        castling = []
        movement = []

        cases = [[1, 1], [-1, 1], [-1, -1], [1, -1], [1, 0], [0, 1], [-1, 0], [0, -1]]

        for e1, e2 in cases:
            di = [[yPos, xPos]]
            while 0 <= di[-1][0] + e1 < 8 and 0 <= di[-1][1] + e2 < 8 and mapGame[di[-1][0] + e1][di[-1][1] + e2] == 0:
                di += [[di[-1][0] + e1, di[-1][1] + e2]]
            if 0 <= di[-1][0] + e1 < 8 and 0 <= di[-1][1] + e2 < 8 and mapGame[di[-1][0] + e1][di[-1][1] + e2].color != self.color:
                eat += [[di[-1][0] + e1, di[-1][1] + e2]]
            movement += di[1:]

        return movement, eat, castling, []
