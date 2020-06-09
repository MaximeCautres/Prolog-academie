from copy import deepcopy

class Game:
    def __init__(self, board, client):
        self.board = board
        self.client = client
        self.inGame = True
        self.selected

    def launchGame(self):
        while self.inGame:
            self.task()

    def task(self): # a list of task

        what_action = self.client.received_action() # the filter to know which task will be done

        if what_action == "Event": # The player will select a piece
        
            event = self.board.getEvent()

            self.client.sendEvent(event)


        if what_action == "ApplySelection": # The player selected the piece, time to update futur possible positions
            
            selectElement, movement, eat, castling, enPassant = self.client.recvApplySelection()
            self.board.applySelection(selectElement, movement, eat, castling, enPassant)

        if what_action == "UpdateDisplay": # The round is finish, time to update the board
            to_update = self.client.recvUpdateDisplay() 
            
            self.board.updateDisplay(to_update)
            
        if what_action == "PieceMovement":
            moves = self.client.recvPieceMovement()

            ''' Sur les client plus la peine d'avoir des objet dans le tableau!!!!!! Plus que les piectype <3 <3 <3 <3 Il faudra ensuite adapter les fonction d'affichage au faite que c'est ça mais nikel que ça marche'''

            for newJ, newI, oldJ, oldI in moves:
                self.board.map[newJ][newI] = deepcopy(self.board.map[oldJ][I])
                self.board.map[oldJ][oldI] = None
            


        if what_action == "PieceSuppression":


        if what_action == "PawnArrival":


        if what_action == 'Check':
            print("You are check, protect your king!")

            
        
            
        
