class Fou:
    def __init__(self, couleur):
        self.couleur = couleur
        self.piecetype = 'fou'

    # On retourne les positions ou peut se déplacer la tour avec ou sans manger
    def deplacement(self, y, x, partie):
        carte = partie.map
        manger = []
        roque = []
        mouvement = []

        cas = [[1, 1], [-1, 1], [-1, -1], [1, -1]]

        for e1, e2 in cas:
            di = [[y, x]]
            while 0 <= di[-1][0] + e1 < 8 and 0 <= di[-1][1] + e2 < 8 and carte[di[-1][0] + e1][di[-1][1] + e2] == 0:
                di += [[di[-1][0] + e1, di[-1][1] + e2]]
            if 0 <= di[-1][0] + e1 < 8 and 0 <= di[-1][1] + e2 < 8and carte[di[-1][0] + e1][di[-1][1] + e2].couleur != self.couleur:
                manger += [[di[-1][0] + e1, di[-1][1] + e2]]
            mouvement += di[1:]

        return mouvement, manger, roque, []
