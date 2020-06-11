import pygame

from copy import deepcopy

from classes.bishop import Bishop
from classes.king import King
from classes.knight import Knight
from classes.pawn import Pawn
from classes.queen import Queen
from classes.rook import Rook

from network.server import Server
from brain.board import Board
from brain.game import Game

host = "192.168.1.19"
port = 50000

if __name__ == "__main__":

    server = Server(host, port, 2)
    server.connexion_of_client()
    board = Board()
    game = Game(board, server)
    game.launchGame()

    server.mySocket.close()
