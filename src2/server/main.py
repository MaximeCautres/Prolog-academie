from network.server import Server

host = "192.168.1.19"
port = 50000

if __name__ == "__main__":

    server = Server(host, port, 2)
    server.connexion_of_client()
    server.mySocket.close()
