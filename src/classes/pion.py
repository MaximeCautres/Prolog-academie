class Pion:
    def __init__(self, couleur):
        self.couleur = couleur
        self.piecetype = 'pion'
        self.bouge_2 = -10

    # On renvoie les positions possibles avec ou sans manger pour un pion
    def deplacement(self, y, x, partie):
        carte = partie.map
        mouvement = []
        manger = []
        roque = []
        passant = []

        times = 1 if self.couleur == 'blanc' else -1

        # On gère le deplacement
        if 0 <= y + times < 8 and carte[y + times][x] == 0:
                mouvement += [[y + times, x]]
                if y == (1 if self.couleur == 'blanc' else 6) and carte[y + times * 2][x] == 0:
                    mouvement += [[y + times * 2, x]]

        cas = [1, -1]
        # On gère le mangeage classique
        for e in cas:
            if 0 <= y + times < 8 and 0 <= x + e < 8 and carte[y + times][x + e] != 0:
                if carte[y + times][x + e].couleur != self.couleur:
                    manger += [[y + times, x + e]]

        # On gère la prise par passant
        for e in cas:
            if y == (4 if self.couleur == 'blanc' else 3) and 0 <= x + e < 8 and carte[y + times][x + e] == 0:
                if carte[y][x + e] != 0 and carte[y][x + e].couleur != self.couleur and carte[y][x + e].piecetype == 'pion' and carte[y][x + e].bouge_2 == partie.numero_tour - 1:
                    passant += [[y + times, x + e]]

        return mouvement, manger, roque, passant
