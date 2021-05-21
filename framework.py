"""
This is the framework for UDPClient, adapted from Assignment 1.
"""

from socket import *        # Used to create sockets.
serverName = "127.0.0.1"    # Sets name of server to hostname (DNS will provide IP of localhost)
serverPort = 12000          # Sends to arbitrary port number of 1200 (to avoid well known hosts)

for pingnum in range(1,11):

    """
    This sends 10 pings in a loop, starting at 1. There needs to be a timeout exception otherwise
    the program will freeze (block/wait for lost packet from server.
    """

    print(f"Loop #:{pingnum}")
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    message = f"Ping{pingnum}"
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    clientSocket.close()


