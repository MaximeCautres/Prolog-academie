import os
import pygame

import matplotlib.image as mpimg
import numpy as np

from pygame.local import *
from copy import deepcopy

from classes.bishop import bishop
from classes.king import king
from classes.knight import knight
from classes.pawn import pawn
from classes.queen import queen
from classes.rook import rook

from GUI.plateau import plateau



unit = 100

if __name__ == "__main__":
    pygame.init()
