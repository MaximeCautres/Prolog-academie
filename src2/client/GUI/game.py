from copy import deepcopy

class Game:
    def __init__(self, board, client):
        self.board = board
        self.client = client
        self.inGame = True

    def launchGame(self):
        while self.inGame:
            self.task()

    def task(self): # a list of task

        what_action = self.client.recvSignal() # the filter to know which task will be done

        if what_action == "Event": # The player will select a piece

            print("It's your turn")
            
            event = self.board.getEvent()

            self.client.sendEvent(event)


        if what_action == "ApplySelection": # The player selected the piece, time to update futur possible positions
            
            selectElement, movement, eat, castling, enPassant = self.client.recvApplySelection()
            self.board.applySelection(selectElement, movement, eat, castling, enPassant)

        if what_action == "UpdateDisplay": # The round is finish, time to update the board
            to_update = self.client.recvInformation() 
            
            self.board.updateDisplay(to_update)
            
        if what_action == "PieceMovement":
            moves = self.client.recvInformation()

            for color, newJ, newI, oldJ, oldI in moves:
                self.board.map[newJ][newI] = deepcopy(self.board.map[oldJ][oldI])
                self.board.map[oldJ][oldI] = None

                self.board.pieces[color].remove([oldJ, oldI])
                self.board.pieces[color] += [[newJ, newI]]
            
        if what_action == "PieceSuppression":
            suppr = self.client.recvInformation()

            for color, j, i in suppr:
                self.board.pieces[color].remove([j, i])


        if what_action == "PawnArrival":
            j, i = self.client.recvInformation()

            n = 0
            while not 0 < n < 5:
                n = input(
                    "Promotion !!  1- Queen, 2-Bishop, 3-Knight, 4-Rook: "
                )
                try:
                    n = int(n)
                except:
                    print(
                        "Entry not valid (must be between 1 and 4)"
                    )
                    n = 0

            self.client.sendEvent(n)

        if what_action == "Change":
            color, j, i, piece = self.client.recvInformation()
            print(piece)
            self.board.map[j][i] = (piece, color)

        if what_action == 'Check':
            print("You are check, protect your king!")
            self.client.sendEvent("go")

        if what_action == "EndGame":
            self.inGame = False
            print("EndGame")

            
        
            
        
