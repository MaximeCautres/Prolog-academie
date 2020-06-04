from classes.piece import Piece

class Queen(Piece):
    def __init__(self, color, xPos, yPos):
        Piece.__init__(self, color, xPos, yPos)
        self.colors = color
        self.piecetype = 'queen'

    # Return position where can move
    def getMove(self, game):

        yPos, xPos = self.yPos, self.xPos

        mapGame = game.map
        eat = []
        castling = []
        movement = []

        cases = [[1, 1], [-1, 1], [-1, -1], [1, -1], [1, 0], [0, 1], [-1, 0], [0, -1]]

        for y, x in cases:
            directionMovement = [[yPos, xPos]]
            while 0 <= directionMovement[-1][0] + y < 8 and 0 <= directionMovement[-1][1] + x < 8 and mapGame[directionMovement[-1][0] + y][directionMovement[-1][1] + x] == 0:
                directionMovement += [[directionMovement[-1][0] + y, directionMovement[-1][1] + x]]
            if 0 <= directionMovement[-1][0] + y < 8 and 0 <= directionMovement[-1][1] + x < 8 and mapGame[directionMovement[-1][0] + y][directionMovement[-1][1] + x].color != self.color:
                eat += [[directionMovement[-1][0] + y, directionMovement[-1][1] + x]]
            movement += directionMovement[1:]

        return movement, eat, castling, []
