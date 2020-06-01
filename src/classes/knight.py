class Knight(Piece):
    def __init__(self, color, xPos, yPos):
        Piece.__init__(self, color, xPos, yPos)
        self.piecetype = 'knight'

    # Return movement where the knight can move
    def move(self, yPos, xPos, game):
        mapGame = game.map
        eat = []
        movement = []
        castling = []

        cases = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

        for e1, e2 in cases:
            if 0 <= yPos + e1 < 8 and 0 <= xPos + e2 < 8 and mapGame[yPos + e1][xPos + e2] == 0:
                movement += [[yPos + e1, xPos + e2]]
            elif 0 <= yPos + e1 < 8 and 0 <= xPos + e2 < 8 and mapGame[yPos + e1][xPos + e2].color != self.color:
                eat += [[yPos +e1, xPos + e2]]

        return movement, eat, castling, []
