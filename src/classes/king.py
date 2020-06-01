class King(Piece):
    def __init__(self, color, xPos, yPos):
        Piece.__init__(self, xPos, yPos, color)
        self.moved = False
        self.piecetype = 'king'

    # Return the king position with or without eating
    def get_move(self, yPos, xPos, game):
        mapGame = game.map
        eat = []
        movement = []
        castling = []

        cases = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

        for e1, e2 in cases:
            if 0 <= yPos + e1 < 8 and 0 <= xPos + e2 < 8 and mapGame[yPos + e1][xPos + e2] == 0:
                movement += [[yPos + e1, xPos + e2]]
            elif 0 <= yPos + e1 < 8 and 0 <= xPos + e2 < 8 and mapGame[yPos + e1][xPos + e2].color != self.color:
                eat += [[yPos + e1, xPos + e2]]

        return movement, eat, castling, []
