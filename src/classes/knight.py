from classes.piece import Piece

class Knight(Piece):
    def __init__(self, color, xPos, yPos):
        Piece.__init__(self, color, xPos, yPos)
        self.piecetype = 'knight'

    # Return movement where the knight can move
    def getMove(self, game, check):

        yPos, xPos = self.yPos, self.xPos

        mapGame = game.map
        eat = []
        movement = []
        castling = []

        cases = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

        for y, x in cases:
            if 0 <= yPos + y < 8 and 0 <= xPos + x < 8 and mapGame[yPos + y][xPos + x] == None:
                movement += [[yPos + y, xPos + x]]
            elif 0 <= yPos + y < 8 and 0 <= xPos + x < 8 and mapGame[yPos + y][xPos + x].color != self.color:
                eat += [[yPos +y, xPos + x]]

        return movement, eat, castling, []
