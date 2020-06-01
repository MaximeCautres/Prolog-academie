class Roi:
    def __init__(self, couleur):
        self.abouge = False
        self.couleur = couleur
        self.piecetype = 'roi'

    # On retourne la position du roi avec ou sans manger
    def deplacement(self, y, x, parite):
        carte = partie.map
        manger = []
        mouvement = []
        roque = []

        cas = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]

        for e1, e2 in cas:
            if 0 <= y + e1 < 8 and 0 <= x + e2 < 8 and carte[y + e1][x + e2] == 0:
                mouvement += [[y + e1, x + e2]]
            elif 0 <= y + e1 < 8 and 0 <= x + e2 < 8 and carte[y + e1][x + e2].couleur != self.couleur:
                manger += [[y + e1, x + e2]]

        return mouvement, manger, roque, []
