class King:
    def __init__(self, color):
        self.moved = False
        self.color = color
        self.piecetype = 'king'

    # On retourne la position du roi avec ou sans manger
    # Return the king position with or without eating
    def move(self, y, x, game):
        mapGame = game.map
        eat = []
        movement = []
        castling = []

        cases = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

        for e1, e2 in cas:
            if 0 <= y + e1 < 8 and 0 <= x + e2 < 8 and mapGame[y + e1][x + e2] == 0:
                movement += [[y + e1, x + e2]]
            elif 0 <= y + e1 < 8 and 0 <= x + e2 < 8 and mapGame[y + e1][x + e2].color != self.color:
                eat += [[y + e1, x + e2]]

        return movement, eat, castling, []
