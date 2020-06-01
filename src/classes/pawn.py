class Pawn(Piece):
    def __init__(self, color, xPos, yPos):
        Piece.__init__(self, color xPos, yPos)
        self.piecetype = 'pawn'
        self.moved = -10

    # return possible positions
    def move(self, yPos, xPos, game):
        mapGame = game.map
        movement = []
        eat = []
        castling = []
        enPassant = []

        times = 1 if self.color == 'white' else -1

        # Movement
        if 0 <= yPos + times < 8 and carte[yPos + times][xPos] == 0:
                movement += [[yPos + times, xPos]]
                if yPos == (1 if self.color == 'white' else 6) and mapGame[yPos + times * 2][xPos] == 0:
                    movement += [[yPos + times * 2, xPos]]

        cases = [1, -1]

        # Classic eating
        for e in cases:
            if 0 <= yPos + times < 8 and 0 <= xPos + e < 8 and mapGame[yPos + times][xPos + e] != 0:
                if mapGame[yPos + times][xPos + e].color != self.color:
                    eat += [[yPos + times, xPos + e]]

        # "en passant"
        for e in cases:
            if yPos == (4 if self.color == 'white' else 3) and 0 <= xPos + e < 8 and mapGame[yPos + times][xPos + e] == 0:
                if mapGame[yPos][xPos + e] != 0 and mapGame[yPos][xPos + e].color != self.color and mapGame[yPos][xPos + e].piecetype == 'pown' and mapGame[yPos][xPos + e].moved == game.round_number - 1:
                    enPassant += [[yPos + times, xPos + e]]

        return movement, eat, castling, enPassant
