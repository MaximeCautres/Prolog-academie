# Client


import os
import pygame

import numpy as np
import matplotlib.image as mpimg

from pygame.locals import *

class Board:
    def __init__(self, unit, color):
        # Create the table which represents the board
        self.map = [[None for _ in range(8)] for _ in range(8)]
        
        # Initialization of the board with all the pieces
        for x in range(8):
            self.map[1][x] = ('pawn', True)
            self.map[6][x] = ('pawn', False)
        self.map[0][0] = ('rook', True)
        self.map[0][7] = ('rook', True)
        self.map[7][0] = ('rook', False)
        self.map[7][7] = ('rook', False)
        self.map[0][1] = ('knight', True)
        self.map[0][6] = ('knight', True)
        self.map[7][1] = ('knight', False)
        self.map[7][6] = ('knight', False)
        self.map[0][2] = ('bishop', True)
        self.map[0][5] = ('bishop', True)
        self.map[7][2] = ('bishop', False)
        self.map[7][5] = ('bishop', False)
        self.map[0][3] = ('queen', True)
        self.map[7][3] = ('queen', False)
        self.map[0][4] = ('king', True)
        self.map[7][4] = ('king', False)

        # Positions of all the pieces at the beginning of the games.
        # It changes with pieces' moves
        self.pieces = {
            True: [[0, x] for x in range(8)] + [[1, x] for x in range(8)],
            False: [[6, x] for x in range(8)] + [[7, x] for x in range(8)],
        }

        self.unit = unit
        self.color = color

    def display(self):
        # the window is created
        self.window = pygame.display.set_mode((self.unit * 8, self.unit * 8))

        # Creation of the board's visual
        background = np.zeros((self.unit * 8, self.unit * 8, 3), dtype=np.uint8)
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    background[
                        i * self.unit : (i + 1) * self.unit,
                        j * self.unit : (j + 1) * self.unit,
                    ] = np.array([240, 209, 136])
                else:
                    background[
                        i * self.unit : (i + 1) * self.unit,
                        j * self.unit : (j + 1) * self.unit,
                    ] = np.array([102, 51, 0])

        mpimg.imsave("background.png", background)

        # Creation of the board's visual annexes
        mpimg.imsave(
            "whiteCase.png",
            np.array(
                [[[240, 209, 136] for _ in range(self.unit)] for _ in range(self.unit)],
                dtype=np.uint8,
            ),
        )
        mpimg.imsave(
            "blackCase.png",
            np.array(
                [[[102, 51, 0] for _ in range(self.unit)] for _ in range(self.unit)],
                dtype=np.uint8,
            ),
        )
        mpimg.imsave(
            "movementCase.png",
            np.array(
                [
                    [[128, 109, 90, 150] for _ in range(self.unit)]
                    for _ in range(self.unit)
                ],
                dtype=np.uint8,
            ),
        )
        mpimg.imsave(
            "eatCase.png",
            np.array(
                [
                    [[165, 38, 10, 100] for _ in range(self.unit)]
                    for _ in range(self.unit)
                ],
                dtype=np.uint8,
            ),
        )
        mpimg.imsave(
            "selectCase.png",
            np.array(
                [
                    [[1, 215, 88, 80] for _ in range(self.unit)]
                    for _ in range(self.unit)
                ],
                dtype=np.uint8,
            ),
        )
        mpimg.imsave(
            "castlingCase.png",
            np.array(
                [
                    [[255, 215, 0, 60] for _ in range(self.unit)]
                    for _ in range(self.unit)
                ],
                dtype=np.uint8,
            ),
        )

        # We load annexes and background for futur uses
        self.background = pygame.image.load("background.png").convert()
        self.whiteCase = pygame.image.load("whiteCase.png").convert()
        self.blackCase = pygame.image.load("blackCase.png").convert()
        self.movementCase = pygame.image.load("movementCase.png").convert_alpha()
        self.eatCase = pygame.image.load("eatCase.png").convert_alpha()
        self.selectCase = pygame.image.load("selectCase.png").convert_alpha()
        self.castlingCase = pygame.image.load("castlingCase.png").convert_alpha()

        self.pieces_skin = {
            "pawn": {
                True: pygame.transform.scale(
                    pygame.image.load("pictures/whitePawn.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
                False: pygame.transform.scale(
                    pygame.image.load("pictures/blackPawn.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
            },
            "rook": {
                True: pygame.transform.scale(
                    pygame.image.load("pictures/whiteRook.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
                False: pygame.transform.scale(
                    pygame.image.load("pictures/blackRook.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
            },
            "knight": {
                True: pygame.transform.scale(
                    pygame.image.load("pictures/whiteKnight.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
                False: pygame.transform.scale(
                    pygame.image.load("pictures/blackKnight.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
            },
            "bishop": {
                True: pygame.transform.scale(
                    pygame.image.load("pictures/whiteBishop.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
                False: pygame.transform.scale(
                    pygame.image.load("pictures/blackBishop.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
            },
            "king": {
                True: pygame.transform.scale(
                    pygame.image.load("pictures/whiteKing.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
                False: pygame.transform.scale(
                    pygame.image.load("pictures/blackKing.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
            },
            "queen": {
                True: pygame.transform.scale(
                    pygame.image.load("pictures/whiteQueen.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
                False: pygame.transform.scale(
                    pygame.image.load("pictures/blackQueen.png").convert_alpha(),
                    (int(self.unit * 0.8), int(self.unit * 0.8)),
                ),
            },
        }

        # We clean the repository
        """os.system(
            "rm background.png whiteCase.png blackCase.png eatCase.png movementCase.png castlingCase.png selectCase.png"
        )"""

        # We initialize the pygame window
        # pygame.init()

        # We display the board
        self.window.blit(self.background, (0, 0))

        pygame.display.flip()

        # We display the initial board configuration
        to_update = []

        for couleur in self.pieces:
            to_update += self.pieces[couleur]

        self.updateDisplay(to_update)

    def applySelection(self, selectElement, movement, eat, castling, enPassant):
        self.window.blit(
            self.selectCase,
            ((selectElement[1] if self.color else (7 - selectElement[1])) * self.unit, ((7 - selectElement[0]) if self.color else selectElement[0]) * self.unit),
        )
        for y, x in movement:
            self.window.blit(self.movementCase, ((x if self.color else (7-x)) * self.unit, ((7 - y) if self.color else y) * self.unit))
        for y, x in eat:
            self.window.blit(self.eatCase, ((x if self.color else (7-x)) * self.unit, ((7 - y) if self.color else y) * self.unit))
        for y, x in castling:
            self.window.blit(self.castlingCase, ((x if self.color else (7-x)) * self.unit, ((7 - y) if self.color else y) * self.unit))
        for y, x in enPassant:
            self.window.blit(self.eatCase, ((x if self.color else (7-x)) * self.unit, ((7 - y) if self.color else y) * self.unit))
        pygame.display.flip()

    def updateDisplay(self, to_update):
        for y, x in to_update:
            self.window.blit(
                self.whiteCase if (x + y + 1) % 2 == 0 else self.blackCase,
                ((x if self.color else (7-x)) * self.unit, ((7 - y) if self.color else y) * self.unit),
            )
            if self.map[y][x] != None:
                self.window.blit(
                    self.pieces_skin[self.map[y][x][0]][self.map[y][x][1]],
                    (int(((x if self.color else (7-x)) + 0.1) * self.unit), int((((7 - y) if self.color else y) + 0.1) * self.unit)),
                )

        pygame.display.flip()

    def getEvent(self):
        while True:
            for event in pygame.event.get():  # We ask the user to do something
                if event.type == QUIT:  # We close the pygame window
                    pygame.quit()
                    return False
                if (
                    event.type == MOUSEBUTTONDOWN and event.button == 1
                ):  # We return the coordonate of the click
                    x, y = event.pos
                    return ((7 - y // self.unit) if self.color else (y // self.unit)), ((x // self.unit) if self.color else (7 - x // self.unit))
