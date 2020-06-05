from classes.piece import Piece

class Rook(Piece):
    def __init__(self, color, xPos, yPos):
        Piece.__init__(self, color, xPos, yPos)
        self.moved = False
        self.piecetype = 'rook'

    # On retourne les position ou peu se déplacer la tour avec ou sans manger
    def getMove(self, game, check):

        yPos, xPos = self.yPos, self.xPos

        mapGame = game.map
        eat = []
        castling = []
        movement = []

        cases = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        for y, x in cases:
            directionMovement = [[yPos, xPos]]
            while 0 <= directionMovement[-1][0] + y < 8 and 0 <= directionMovement[-1][1] + x < 8 and mapGame[directionMovement[-1][0] + y][directionMovement[-1][1] + x] == None:
                directionMovement += [[directionMovement[-1][0] + y, directionMovement[-1][1] + x]]
            if 0 <= directionMovement[-1][0] + y < 8 and 0 <= directionMovement[-1][1] + x < 8 and mapGame[directionMovement[-1][0] + y][directionMovement[-1][1] + x].color != self.color:
                eat += [[directionMovement[-1][0] + y, directionMovement[-1][1] + x]]
            if 0 <= directionMovement[-1][0] + y < 8 and 0 <= directionMovement[-1][1] + x < 8 and mapGame[directionMovement[-1][0] + y][directionMovement[-1][1] + x].color == self.color and mapGame[directionMovement[-1][0] + y][directionMovement[-1][1] + x].piecetype == 'roi' and not self.moved and not mapGame[directionMovement[-1][0] + y][directionMovement[-1][1] + x].moved:
                castling += [[directionMovement[-1][0] + y, directionMovement[-1][1] + x]]
            movement += directionMovement[1:]

        return movement, eat, [], []
