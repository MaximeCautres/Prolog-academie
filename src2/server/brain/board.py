import os
import pygame

import numpy as np
import matplotlib.image as mpimg

from pygame.locals import *

from classes.bishop import Bishop
from classes.king import King
from classes.knight import Knight
from classes.pawn import Pawn
from classes.queen import Queen
from classes.rook import Rook


class Board:
    def __init__(self, unit):
        # Create the table which represents the board
        self.map = [[None for _ in range(8)] for _ in range(8)]

        # Initialization of the board with all the pieces
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
        self.map[7][2] = Bishop(False, 2, 7)
        self.map[7][5] = Bishop(False, 5, 7)
        self.map[0][3] = Queen(True, 3, 0)
        self.map[7][3] = Queen(False, 3, 7)
        self.map[0][4] = King(True, 4, 0)
        self.map[7][4] = King(False, 4, 7)

        # Initialization of the round_number
        self.roundNumber = 0

        # Positions of all the pieces at the beginning of the games.
        # It changes with pieces' moves
        self.pieces = {
            True: [[0, x] for x in range(8)] + [[1, x] for x in range(8)],
            False: [[6, x] for x in range(8)] + [[7, x] for x in range(8)],
        }

        # The kings will need to be track during the game for the check detection
        self.king = {True: [0, 4], False: [7, 4]}
        self.unit = unit

    
