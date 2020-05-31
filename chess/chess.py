# ici ça part sur une implémentation de jeu d'échec
from copy import deepcopy

unit = 100

class Pion:
    def __init__(self, couleur):
        self.couleur = couleur
        self.piecetype = 'pion'
        self.bouge_2 = -10

    def deplacement(self, y, x, partie): # renvoie les positions possibles avec ou sans manger pour un poin
        carte = partie.map
        
        mouvement = []
        manger = []
        roque = []
        passant = []

        times = 1 if self.couleur == 'blanc' else -1

        if 0 <= y + times < 8 and carte[y + times][x] == 0: # On gère le deplacement
                mouvement += [[y + times, x]]
                if y == (1 if self.couleur == 'blanc' else 6) and carte[y + times * 2][x] == 0:
                    mouvement += [[y + times * 2, x]]

        cas = [1, -1]
        for e in cas: # On gère le mangeage classique
            if 0 <= y + times < 8 and 0 <= x + e < 8 and carte[y + times][x + e] != 0:
                if carte[y + times][x + e].couleur != self.couleur:
                    manger += [[y + times, x + e]]

        for e in cas: # On gère la prise par passant
            if y == (4 if self.couleur == 'blanc' else 3) and 0 <= x + e < 8 and carte[y + times][x + e] == 0:
                if carte[y][x + e] != 0 and carte[y][x + e].couleur != self.couleur and carte[y][x + e].piecetype == 'pion' and carte[y][x + e].bouge_2 == partie.numero_tour - 1:
                    passant += [[y + times, x + e]]


        return mouvement, manger, roque, passant

    
class Tour:
    def __init__(self, couleur):
        self.abouge = False
        self.couleur = couleur
        self.piecetype = 'tour'

    def deplacement(self, y, x, partie): # retourne les position ou peu se déplacer la tour avec ou sans manger
        carte = partie.map
        
        manger = []
        roque = []
        mouvement = []

        cas = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    
        for e1, e2 in cas:       
            di = [[y, x]]
            while 0 <= di[-1][0] + e1 < 8 and 0 <= di[-1][1] + e2 < 8 and carte[di[-1][0] + e1][di[-1][1] + e2] == 0:
                di += [[di[-1][0] + e1, di[-1][1] + e2]]
            if 0 <= di[-1][0] + e1 < 8 and 0 <= di[-1][1] + e2 < 8 and carte[di[-1][0] + e1][di[-1][1] + e2].couleur != self.couleur:
                manger += [[di[-1][0] + e1, di[-1][1] + e2]]
            if 0 <= di[-1][0] + e1 < 8 and 0 <= di[-1][1] + e2 < 8 and carte[di[-1][0] + e1][di[-1][1] + e2].couleur == self.couleur and carte[di[-1][0] + e1][di[-1][1] + e2].piecetype == 'roi' and not self.abouge and not carte[di[-1][0] + e1][di[-1][1] + e2].abouge:
                roque += [[di[-1][0] + e1, di[-1][1] + e2]]
            mouvement += di[1:]
            
        return mouvement, manger, roque, []

    
class Cavalier:
    def __init__(self, couleur):
        self.couleur = couleur
        self.piecetype = 'cavalier'

    def deplacement(self, y, x, partie): # retourne les déplacement possible ou peu se deplacer le cheval avec ou sans manger
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

    
class Fou:
    def __init__(self, couleur):
        self.couleur = couleur
        self.piecetype = 'fou'

    def deplacement(self, y, x, partie): # retourne les position ou peu se déplacer la tour avec ou sans manger
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



class Roi:
    def __init__(self, couleur):
        self.abouge = False
        self.couleur = couleur
        self.piecetype = 'roi'

    def deplacement(self, y, x, parite): # On retourne la position du roi avec ou sans manger
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

    
class Renne:
    def __init__(self, couleur):
        self.couleur = couleur
        self.piecetype = 'renne'

    def deplacement(self, y, x, partie): # retourne les position ou peu se déplacer la tour avec ou sans manger
        carte = partie.map
        
        manger = []
        roque = []
        mouvement = []

        cas = [[1, 1], [-1, 1], [-1, -1], [1, -1], [1, 0], [0, 1], [-1, 0], [0, -1]]
    
        for e1, e2 in cas:       
            di = [[y, x]]
            while 0 <= di[-1][0] + e1 < 8 and 0 <= di[-1][1] + e2 < 8 and carte[di[-1][0] + e1][di[-1][1] + e2] == 0:
                di += [[di[-1][0] + e1, di[-1][1] + e2]]
            if 0 <= di[-1][0] + e1 < 8 and 0 <= di[-1][1] + e2 < 8and carte[di[-1][0] + e1][di[-1][1] + e2].couleur != self.couleur:
                manger += [[di[-1][0] + e1, di[-1][1] + e2]]
            mouvement += di[1:]
            
        return mouvement, manger, roque, []
        

class Plateau:
    
    def __init__(self):
        #self.skin = skin
        self.map = [[0 for _ in range(8)] for _ in range(8)]

        for x in range(8):
            self.map[1][x] = Pion('blanc')
            self.map[6][x] = Pion('noir')
        self.map[0][0] = Tour('blanc')
        self.map[0][7] = Tour('blanc')
        self.map[7][0] = Tour('noir')
        self.map[7][7] = Tour('noir')
        self.map[0][1] = Cavalier('blanc')
        self.map[0][6] = Cavalier('blanc')
        self.map[7][1] = Cavalier('noir')
        self.map[7][6] = Cavalier('noir')
        self.map[0][2] = Fou('blanc')
        self.map[0][5] = Fou('blanc')
        self.map[7][2] = Fou('noir')
        self.map[7][5] = Fou('noir')
        self.map[0][3] = Renne('blanc')
        self.map[7][3] = Renne('noir')
        self.map[0][4] = Roi('blanc')
        self.map[7][4] = Roi('noir')

        #self.map[4][4] = Pion('blanc')

        self.numero_tour = 0 
        self.abandon = False # c'est petit mais le echec et mate c'est chiant à mettre en place
        self.piece = {'blanc': [[0, x] for x in range(8)] + [[1, x] for x in range(8)],
                      'noir': [[6, x] for x in range(8)] + [[7, x] for x in range(8)]
        }
        self.roi = {'blanc': [0, 4], 'noir': [7, 4]}

partie = Plateau()
#print(partie.map[1][4].deplacement(1, 4, partie.map))

import os
import pygame
from pygame.locals import *
pygame.init()

import matplotlib.image as mpimg
import numpy as np

# Ici on génère le fond, i.e. le plateau

plateau = np.zeros((unit*8, unit*8, 3), dtype=np.uint8)
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            plateau[i*unit:(i+1)*unit, j*unit:(j+1)*unit] = np.array([240, 209, 136])
        else:
            plateau[i*unit:(i+1)*unit, j*unit:(j+1)*unit] = np.array([102, 51, 0])
mpimg.imsave("background.png", plateau)

mpimg.imsave("case_beige.png", np.array([[[240, 209, 136] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))
mpimg.imsave("case_marron.png", np.array([[[102, 51, 0] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))
mpimg.imsave("case_deplacement.png", np.array([[[128, 109, 90, 150] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))
mpimg.imsave("case_mangeage.png", np.array([[[165, 38, 10, 100] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))
mpimg.imsave("case_selectionne.png", np.array([[[1, 215, 88, 80] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))
mpimg.imsave("case_roque.png", np.array([[[255, 215, 0, 60] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))




# Ici, on s'occupe de l'interface pygame

fenetre = pygame.display.set_mode((unit*8, unit*8))

fond = pygame.image.load("background.png").convert()
fenetre.blit(fond, (0, 0))
case_beige = pygame.image.load("case_beige.png").convert()
case_marron = pygame.image.load("case_marron.png").convert()
case_deplacement = pygame.image.load("case_deplacement.png").convert_alpha()
case_mangeage = pygame.image.load("case_mangeage.png").convert_alpha()
case_selectionne = pygame.image.load("case_selectionne.png").convert_alpha()
case_roque = pygame.image.load("case_roque.png").convert_alpha()


pion_blanc = pygame.transform.scale(pygame.image.load("pion_blanc.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))
pion_noir = pygame.transform.scale(pygame.image.load("pion_noir.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))
tour_blanc = pygame.transform.scale(pygame.image.load("tour_blanc.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))
tour_noir = pygame.transform.scale(pygame.image.load("tour_noir.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))
cavalier_blanc = pygame.transform.scale(pygame.image.load("cheval_blanc.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))
cavalier_noir = pygame.transform.scale(pygame.image.load("cheval_noir.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))
fou_blanc = pygame.transform.scale(pygame.image.load("fou_blanc.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))
fou_noir = pygame.transform.scale(pygame.image.load("fou_noir.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))
roi_blanc = pygame.transform.scale(pygame.image.load("roi_blanc.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))
roi_noir = pygame.transform.scale(pygame.image.load("roi_noir.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))
renne_blanc = pygame.transform.scale(pygame.image.load("renne_blanc.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))
renne_noir = pygame.transform.scale(pygame.image.load("renne_noir.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))


piece_skin = {'pion': {'blanc': pion_blanc, 'noir': pion_noir},
         'tour': {'blanc': tour_blanc, 'noir': tour_noir},
         'cavalier': {'blanc': cavalier_blanc, 'noir': cavalier_noir},
         'fou': {'blanc': fou_blanc, 'noir': fou_noir},
         'roi': {'blanc': roi_blanc, 'noir': roi_noir},
         'renne': {'blanc': renne_blanc, 'noir': renne_noir}}

def affiche_piece(y, x):
    fenetre.blit(case_beige if (x+y+1)%2 == 0 else case_marron, (x*unit, (7-y) * unit))
    if partie.map[y][x] != 0:
        fenetre.blit(piece_skin[partie.map[y][x].piecetype][partie.map[y][x].couleur], (int((x+0.1) * unit), int((7-y + 0.1) * unit)))
        
    return 

for couleur in partie.piece:
    for y, x in partie.piece[couleur]:
        affiche_piece(y, x)

pygame.display.flip()

continuer = 1
selectionee = False
role = []
echec = False
joueur = 'blanc'
adversaire = 'noir'
print(f'Au tour de {joueur} de jouer')

while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        # continuer = 0 if input() == 'abandon' else 1  
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            i, j = x // unit, 7 - y // unit
            if not selectionee:     # ici, on choisi un de nos pion
                if partie.map[j][i] != 0 and partie.map[j][i].couleur == joueur:
                    fenetre.blit(case_selectionne, (i*unit, (7-j) * unit))
                    mouvement, manger, roque, passant = partie.map[j][i].deplacement(j, i, partie)
                    for cj, ci in mouvement:
                        fenetre.blit(case_deplacement, (ci*unit, (7-cj) * unit))
                    for cj, ci in manger:
                        fenetre.blit(case_mangeage, (ci*unit, (7-cj) * unit))
                    for cj, ci in roque:
                        fenetre.blit(case_roque, (ci*unit, (7-cj) * unit))
                    for cj, ci in passant:
                        fenetre.blit(case_mangeage, (ci*unit, (7-cj) * unit))
                        
                    selectionee = [j, i]
                    role = manger + mouvement + roque + passant

            else: # Ici, on fait une actions
                if [j, i] in role: # Soit on deplace
                    backup = deepcopy(partie)
                    if echec:
                        print("Vous etes echec !!")
                    
                    if [j, i] in partie.piece[joueur]: # Si on roque
                        partie.map[j][i], partie.map[selectionee[0]][selectionee[1]] = deepcopy(partie.map[selectionee[0]][selectionee[1]]), deepcopy(partie.map[j][i])
                        partie.map[j][i].abouge = True
                        partie.map[selectionee[0]][selectionee[1]].abouge = True
                        partie.roi[joueur] = selectionee
                        
                    else: # Si on roque pas
                        partie.map[j][i] = deepcopy(partie.map[selectionee[0]][selectionee[1]])
                        partie.map[selectionee[0]][selectionee[1]] = 0
                        partie.piece[joueur].remove(selectionee)
                        partie.piece[joueur]+= [[j, i]]

                        if [j, i] in partie.piece[adversaire]: # Si on mange une piece de l'autre
                            partie.piece[adversaire].remove([j,i])

                        if partie.map[j][i].piecetype == 'pion' and i != selectionee[1] and [j - (1 if joueur == 'blanc' else -1), i] in partie.piece[adversaire]: # Si l'on mange en passant
                            partie.piece[adversaire].remove([j - (1 if joueur == 'blanc' else -1), i])
                            partie.map[j-(1 if joueur == 'blanc' else -1)][i] = 0
                            role += [[j-(1 if joueur == 'blanc' else -1), i]]
                            

                        if partie.map[j][i].piecetype == 'pion' and abs(j - selectionee[0]) == 2:
                            partie.map[j][i].bouge_2 = partie.numero_tour 
                            
                        if partie.roi[joueur] == selectionee: # Si on bouge le roi, on doit interdire le roque
                            partie.roi[joueur] = [j, i]
                            partie.map[j][i].abouge = True

                        if partie.map[j][i] == 'tour':
                            partie.map[j][i].abouge = True

                    echec = False
                    for piece in partie.piece[adversaire]:
                        _, mangeable, _, _ = partie.map[piece[0]][piece[1]].deplacement(piece[0], piece[1], partie)
                        if partie.roi[joueur] in mangeable:
                            echec = True
                            break

                    if echec:
                        partie = deepcopy(backup)
                    else:

                        if j == (7 if joueur == 'blanc' else 0) and partie.map[j][i].piecetype == 'pion':
                            n = 0
                            while not 0 < n < 5:
                                n = input('Promotion !! Rentre 1 pour renne, 2 pour fou, 3 pour cavalier, 4 pour tour :')
                                try :
                                    n = int(n)
                                except:
                                    print("il faut mettre un entier entre 1 et 4")
                                    n = 0                                    
                                if n == 1:
                                    partie.map[j][i] = Renne(joueur)
                                elif n == 2:
                                    partie.map[j][i] = Fou(joueur)
                                elif n == 3:
                                    partie.map[j][i] = Cavalier(joueur)
                                else:
                                    partie.map[j][i] = Tour(joueur)
                                    partie.map[j][i].abouge = True
                        
                        for j, i in [selectionee]+role: # On change de tour, on refait l'echequier propre
                            affiche_piece(j, i)
                        
                        selectionee = False # Comme on change de tour on deselectionne

                        for piece in partie.piece[joueur]:
                            _, mangeable, _, _ = partie.map[piece[0]][piece[1]].deplacement(piece[0], piece[1], partie)
                            if partie.roi[adversaire] in mangeable:
                                echec = True
                                break

                        partie.numero_tour += 1

                        joueur, adversaire = adversaire, joueur

                        print(f'Au tour de {joueur} de joueur')
                        
                else: # On annule la selection
                    for j, i in [selectionee]+role:
                        affiche_piece(j, i)
                    selectionee = False
            pygame.display.flip()
            
                

                

os.system("rm background.png case\_beige.png case\_marron.png case\_mangeage.png case\_deplacement.png case\_roque.png case\_selectionne.png") # On netoie la merde que l'on fait


        
