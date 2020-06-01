class Knight:
    def __init__(self, color):
        self.color = color
        self.piecetype = 'knight'

    # Return movement where the knight can move
    def move(self, yPos, xPos, game):
        mapGame = game.map
        eat = []
        movement = []
        castling = []

        cases = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

        for e1, e2 in cases:
            if 0 <= y + e1 < 8 and 0 <= x + e2 < 8 and mapGame[y + e1][x + e2] == 0:
                movement += [[y + e1, x + e2]]
            elif 0 <= y + e1 < 8 and 0 <= x + e2 < 8 and mapGame[y + e1][x + e2].color != self.color:
                eat += [[y +e1, x + e2]]

        return movement, eat, castling, []
