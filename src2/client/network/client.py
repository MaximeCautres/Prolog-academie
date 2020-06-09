import socket, sys

class Client():
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.mySocket.connect((host, port))
        except socket.error:
            print("The connexion failed")
            sys.exit
        print("Connexion with the host is established")

        msgServer1 = self.mySocket.recv(1024).decode("Utf8")

        if msgServer1 == "6":

            colorChoice = -1
            
            while colorChoice not in {0, 1}:
                colorChoice = input("Chose your pieces' color: White -> 1, Black -> 0: ")
                try:
                    colorChoice = int(colorChoice)
                except:
                    colorChoice = -1
                    print("Entry not valid (must be an integer between 0 and 1)")

            self.mySocket.send(str(colorChoice).encode("Utf8"))

            msgServer2 = self.mySocket.recv(1024).decode("Utf8")
            self.color = ("1" == msgServer2)

        else:
            msgServer2 = msgServer1
            self.color = ("1" == msgServer2)

    # beginning of the communication function
            
    def sendEvent(self, event):
        if event:
            self.mySocket.send(f"{y} {x}".encode("Utf8"))
        else:
            self.mySocket.send("False".encode("Utf8"))
        
    def recvApplySelection(self):
        selectElement = eval(self.mySocket.recv(1024).decode("Utf8"))
        movement = eval(self.mySocket.recv(1024).decode("Utf8"))
        eat = eval(self.mySocket.recv(1024).decode("Utf8"))
        castling = eval(self.mySocket.recv(1024).decode("Utf8"))
        enPassant = eval(self.mySocket.recv(1024).decode("Utf8"))
        return selectElement, movement, eat, castling, enPassant

    def recvUpdateDisplay(self):
        return eval(self.mySocket.recv(1024).decode("Utf8"))

    def recvPieceMovement(self):
        return eval(self.mySocket.recv(1024).decode("Utf8"))

    def recvPieceSuppression(self):
        return eval(self.mySocket.recv(1024).decode("Utf8"))

    def recvPawnArrival(self):
        return eval(self.mySocket.recv(1024).decode("Utf8"))

    def recvCheck(self):
        return eval(self.mySocket.recv(1024).decode("Utf8"))

    def recvInformation(self): # Should be capable of remplacing all the other one:
        return eval(mySocket.recv(1024).decode("Utf8"))
        

    
    
