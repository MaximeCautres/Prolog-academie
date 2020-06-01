import os
import pygame

import numpy as np
import matplotlib.image as mpimg

from pygame.locals import *


class Plate:
    def __init__(self, unit)):

        # Create the table which represents the plate
        self.map = [[None for _ in range(8)] for _ in range(8)]

        # Initialization of the plate with all the pieces
        for x in range(8):
            self.map[1][x] = Pawn(True, x, 1)
            self.map[6][x] = Pawn(False, x, 6)
        self.map[0][0] = Rook(True, 0, 0)
        self.map[0][7] = Rook(True, 7, 0)
        self.map[7][0] = Rook(False, 0, 7)
        self.map[7][7] = Rook(False, 7, 7)
        self.map[0][1] = Knight(True, 1, 0)
        self.map[0][6] = Knight(True, 6, 0)
        self.map[7][1] = Knight(False, 1, 7)
        self.map[7][6] = Knight(False, 6, 7)
        self.map[0][2] = Bishop(True, 2, 0)
        self.map[0][5] = Bishop(True, 5, 0)
        self.map[7][2] = Bishop(False, 7, 2)
        self.map[7][5] = Bishop(False, 5, 7)
        self.map[0][3] = Queen(True, 3, 0)
        self.map[7][3] = Queen(False, 3, 7)
        self.map[0][4] = King(True, 4, 0)
        self.map[7][4] = King(False, 4, 7)

        # Initialization of the round_number
        self.round_number = 0

        # Positions of all the pieces at the beginning of the games. It changes with pieces' moves
        self.pieces = {
            True: [[0, x] for x in range(8)] + [[1, x] for x in range(8)],
            False: [[6, x] for x in range(8)] + [[7, x] for x in range(8)]
        }

        # The kings will need to be track during the game for the check detection
        self.king = {True: [0, 4], False: [7, 4]}

        self.unit = unit

        def display(self):

            # Creation of the board's visual

            bakground = np.zeros((unit*8, unit*8, 3), dtype=np.uint8)
            for i in range(8):
                for j in range(8):
                    if (i + j) % 2 == 0:
                        background[i*unit:(i+1)*unit, j*unit:(j+1)*unit] = np.array([240, 209, 136])
                    else:
                        background[i*unit:(i+1)*unit, j*unit:(j+1)*unit] = np.array([102, 51, 0])

            mpimg.imsave("background.png", background)

            # Creation of the board's visual annexes

            mpimg.imsave("white_case.png", np.array([[[240, 209, 136] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))
            mpimg.imsave("black_case.png", np.array([[[102, 51, 0] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))
            mpimg.imsave("movement_case.png", np.array([[[128, 109, 90, 150] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))
            mpimg.imsave("eat_case.png", np.array([[[165, 38, 10, 100] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))
            mpimg.imsave("select_case.png", np.array([[[1, 215, 88, 80] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))
            mpimg.imsave("castling_case.png", np.array([[[255, 215, 0, 60] for _ in range(unit)] for _ in range(unit)], dtype=np.uint8))

            # We load annexes and background for futur uses
            
            self.background = pygame.image.load("background.png").convert()
            self.white_case = pygame.image.load("white_case.png").convert()
            self.black_case = pygame.image.load("black_case.png").convert()
            self.movement_case = pygame.image.load("movement_case.png").convert()
            self.eat_case = pygame.image.load("eat_case.png").convert()
            self.select_case = pygame.image.load("select_case.png").convert()
            self.castling_case = pygame.image.load("castling_case.png").convert()

            self.pieces_skin = {'pawn': {True: pygame.transform.scale(pygame.image.load("../pictures/whitePawn.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) )),
                                        False: pygame.transform.scale(pygame.image.load("../pictures/blackPawn.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))},
                               'rook': {True: pygame.transform.scale(pygame.image.load("../pictures/whiteRook.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) )),
                                        False: pygame.transform.scale(pygame.image.load("../pictures/blackRook.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))},
                               'knight': {True: pygame.transform.scale(pygame.image.load("../pictures/whiteKnight.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) )),
                                          False: pygame.transform.scale(pygame.image.load("../pictures/blackKnight.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))}
                               'bishop': {True: pygame.transform.scale(pygame.image.load("../pictures/whiteBishop.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) )),
                                          False: pygame.transform.scale(pygame.image.load("../pictures/blackBishop.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))},
                               'king': {True: pygame.transform.scale(pygame.image.load("../pictures/whiteKing.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) )),
                                        False: pygame.transform.scale(pygame.image.load("../pictures/blackKing.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))},
                               'queen': {True: pygame.transform.scale(pygame.image.load("../pictures/whiteQueen.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) )),
                                         False: pygame.transform.scale(pygame.image.load("../pictures/blackQueen.png").convert_alpha(), (int(unit * 0.8), int(unit * 0.8) ))}}

            # We clean the repository

            os.system("rm background.png white\_case.png black\_case.png eat\_case.png movement\_case.png castling\_case.png select\_case.png")

            # We initialize the pygame window

            pygame.init()

            # We display the board
            
            self.window = pygame.display.set_mode((unit*8, unit*8))
            self.window.blit(background, (0, 0))

            # We display the initial board configuration

            to_update = []
            
            for couleur in self.pieces:
                to_update += self.pieces[couleur]

            self.update_display(to_update)

            
        def apply_selection(self, movement, eat, castling, enPassant):
            for y, x in movement:
                fenetre.blit(movemeent_case, (i*unit, (7-j) * unit))
            for y, x in eat:
                fenetre.blit(eat_case, (i*unit, (7-j) * unit))
            for y, x in castling:
                fenetre.blit(castling_case, (i*unit, (7-j) * unit))
            for y, x in enPassant:
                fenetre.blit(eat_case, (i*unit, (7-j) * unit))
            pygame.display.flip()
        
        def update_display(self, to_update):
            for y, x in to_update:
                self.window.blit(white_case if (x+y+1)%2 == 0 else black_case,
                                 (x * unit, (7-y) * unit))
                if self.map[y][x] != None:
                    self.window.blit(pieces_skin[self.map[y][x].piecetype][self.map[y][x].couleur], (int((x+0.1) * unit), int((7-y + 0.1) * unit)))

            pygame.display.flip()
        

        
