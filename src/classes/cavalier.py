class Cavalier:
    def __init__(self, couleur):
        self.couleur = couleur
        self.piecetype = 'cavalier'

    # On retourne les déplacements possibles ou peut se deplacer le cheval
    # avec ou sans manger
    def deplacement(self, y, x, partie):
        carte = partie.map
        manger = []
        mouvement = []
        roque = []

        cas = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

        for e1, e2 in cas:
            if 0 <= y + e1 < 8 and 0 <= x + e2 < 8 and carte[y + e1][x + e2] == 0:
                mouvement += [[y + e1, x + e2]]
            elif 0 <= y + e1 < 8 and 0 <= x + e2 < 8 and carte[y + e1][x + e2].couleur != self.couleur:
                manger += [[y +e1, x + e2]]

        return mouvement, manger, roque, []
