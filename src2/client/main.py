from network.client import Client
from GUI.game import Game
from GUI.board import Board

host = "192.168.1.19"
port = 50000
unit = 60

if __name__ == "__main__":

    client = Client(host, port)
    board = Board(unit, client.color)
    board.display()
    game = Game(board, client)
    game.launchGame()
    
    client.mySocket.close()
    
