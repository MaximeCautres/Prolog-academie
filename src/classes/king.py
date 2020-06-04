from classes.piece import Piece

class King(Piece):
    def __init__(self, color, xPos, yPos):
        Piece.__init__(self, color, xPos, yPos)
        self.moved = False
        self.piecetype = 'king'

    # Return the king position with or without eating
    def getMove(self, game):
        yPos, xPos = self.yPos, self.xPos
        mapGame = game.map
        eat = []
        movement = []
        castling = []

        cases = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

        for y, x in cases:
            if 0 <= yPos + y < 8 and 0 <= xPos + x < 8 and mapGame[yPos + y][xPos + x] == 0:
                movement += [[yPos + y, xPos + x]]
            elif 0 <= yPos + y < 8 and 0 <= xPos + x < 8 and mapGame[yPos + y][xPos + x].color != self.color:
                eat += [[yPos + y, xPos + x]]

        return movement, eat, castling, []
