from network.client import Client

host = "192.168.1.19"
port = 50000

if __name__ == "__main__":

    client = Client(host, port)
    print(client.color)
    client.mySocket.close()
    
