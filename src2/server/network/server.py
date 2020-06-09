import socket, sys

class Server():
    def __init__(self, host, port, max_conn):
        self.host = host
        self.port = port
        self.counter = 0
        self.max_conn = max_conn
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        try:
            self.mySocket.bind((host, port))
        except socket.error:
            print("The socket's liaison to the choosen adress failed")
            sys.exit
            
    def connexion_of_client(self):
        while 1:
            print("Wainting the player connexion")
            self.mySocket.listen(5)

            connexion1, adress1 = self.mySocket.accept()
            self.counter += 1

            print(f"Client connected with IP {adress1[0]}, port {adress1[1]}")

            msgServer = "6"
            connexion1.send(msgServer.encode("Utf8"))
            
            connexion2, adress2 = self.mySocket.accept()
            self.counter += 1

            print(f"Client connected with IP {adress2[0]}, port {adress2[1]}")


            colorChoice = 1 if "1" == connexion1.recv(1024).decode("Utf8") else 0

            self.player = {}
            
            if colorChoice:
                self.player[True] = connexion1
                self.player[False] = connexion2
            else:
                self.player[True] = connexion2
                self.player[False] = connexion1

            connexion1.send(str(colorChoice).encode("Utf8"))
            connexion2.send(str(1 - colorChoice).encode("Utf8"))

            return

    # beginning of the communication function
    
    def askEvent(self, color):
        
        self.player[color].send('Event'.encode("Utf8")) #signal

        event = self.player[color].recv(1024).decode("Utf8")
        if event != "False":
            j, i = coordonate[0], coordonate[2]
            return j, i
        else:
            return False

    # share all the piece to color after a selectioon to the corresponding client

    def sendApplySelection(self, color, selectElement, movement, eat, castling, enPassant):
        self.player[color].send("ApplySelection") # signal
        
        self.player[color].send(str(selectElement).encode("Utf8"))
        self.player[color].send(str(movement).encode("Utf8"))
        self.player[color].send(str(eat).encode("Utf8"))
        self.player[color].send(str(castling).encode("Utf8"))
        self.player[color].send(str(enPassant).encode("Utf8"))

        return 

    # Share the update to all the client
    
    def sendUpdateDisplay(self, to_update):
        self.player[True].send("UpdateDisplay".encode("Utf8")) # signal

        self.player[True].send(str(to_update).encode("Utf8"))
        
        self.player[False].send("UpdateDisplay".encode("Utf8")) # signal
        
        self.player[False].send(str(to_update).encode("Utf8"))

    # share the movement of a piece to the client

    def sendPieceMouvement(self, l): # [[newJ, newI, oldJ, oldI], ]
        self.player[True].send("PieceMovement".encode("Utf8")) # signal
        
        self.player[True].send(str(l).encode("Utf8"))

        self.player[False].send("PieceMovement".encode("Utf8")) # signal
        
        self.player[False].send(str(l).encode("Utf8"))

    # Share the suppression of a piece to all the client
    
    def sendPieceSuppression(self, l): #[[color, j, i],]
        self.player[False].send("PieceSuppression".encode("Utf8")) # signal

        self.player[False].send(str(l).encode("Utf8"))

        self.player[True].send("PieceSuppression".encode("Utf8")) # signal
        
        self.player[True].send(str(l).encode("Utf8"))

    # Share the pawn arrival process, choose what you want
    
    def sendPawnArrival(self, color, j, i): # return n the chosen piece
        self.player[color].send("PawnArrival".encode("Utf8")) # signal
        
        self.player[color].send(str([j, i]).encode("Utf8"))

        return eval(self.player[True].recv(1024).decode("Utf8"))

    
    def sendChange(self, color, j, i, piece): # affect the change of both player
        self.player[True].send("Change".encode("Utf8")) # signal

        self.player[True].send(str([j, i, piece]).encode("Utf8"))

        self.player[False].send("Change".encode("Utf8")) # signal

        self.player[False].send(str([j, i, piece]).encode("Utf8"))

        
    # Print your check on the client terminal
    
    def sendCheck(self, color):
        self.player[color].send("Check".encode("Utf8")) # signal
        
    def sendEndGame(self):
        self.player[True].send("EndGame".encode("Utf8")) # signal
        self.player[True].send("EndGame".encode("Utf8")) # signal

