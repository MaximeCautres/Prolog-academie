from classes.piece import Piece

class Pawn(Piece):
    def __init__(self, color, xPos, yPos):
        Piece.__init__(self, color, xPos, yPos)
        self.piecetype = 'pawn'
        self.moved = False
        self.bigMove = - 10

    # return possible positions
    def getMove(self, game):

        yPos, xPos = self.yPos, self.xPos

        mapGame = game.map
        movement = []
        eat = []
        castling = []
        enPassant = []

        times = 1 if self.color else -1

        # Movement
        if 0 <= yPos + times < 8 and mapGame[yPos + times][xPos] == None:
                movement += [[yPos + times, xPos]]
                if yPos == (1 if self.color else 6) and mapGame[yPos + times * 2][xPos] == None:
                    movement += [[yPos + times * 2, xPos]]

        cases = [1, -1]

        # Classic eating
        for e in cases:
            if 0 <= yPos + times < 8 and 0 <= xPos + e < 8 and mapGame[yPos + times][xPos + e] != None:
                if mapGame[yPos + times][xPos + e].color != self.color:
                    eat += [[yPos + times, xPos + e]]

        # "en passant"
        for e in cases:
            if yPos == (4 if self.color else 3) and 0 <= xPos + e < 8 and mapGame[yPos + times][xPos + e] == None:
                if mapGame[yPos][xPos + e] != None and mapGame[yPos][xPos + e].color != self.color and mapGame[yPos][xPos + e].piecetype == 'pawn' and mapGame[yPos][xPos + e].bigMove == game.roundNumber - 1:
                    enPassant += [[yPos + times, xPos + e]]

        return movement, eat, castling, enPassant
