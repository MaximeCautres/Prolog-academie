class Pawn:
    def __init__(self, color):
        self.color = color
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
        if 0 <= y + times < 8 and carte[y + times][x] == 0:
                movement += [[y + times, x]]
                if y == (1 if self.color == 'white' else 6) and mapGame[y + times * 2][x] == 0:
                    movement += [[y + times * 2, x]]

        cases = [1, -1]

        # Classic eating
        for e in cases:
            if 0 <= y + times < 8 and 0 <= x + e < 8 and mapGame[y + times][x + e] != 0:
                if mapGame[y + times][x + e].color != self.color:
                    eat += [[y + times, x + e]]

        # "en passant"
        for e in cases:
            if y == (4 if self.color == 'white' else 3) and 0 <= x + e < 8 and mapGame[y + times][x + e] == 0:
                if mapGame[y][x + e] != 0 and mapGame[y][x + e].color != self.color and mapGame[y][x + e].piecetype == 'pown' and mapGame[y][x + e].moved == game.numero_tour - 1:
                    enPassant += [[y + times, x + e]]

        return movement, eat, castling, enPassant
