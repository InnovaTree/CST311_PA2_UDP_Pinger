"""
NAMES: Larry Chiem, Ian Rowe, Raymond Shum, Nicholas Stankovich
DUE DATE: May 25, 2021
ASSIGNMENT: Team Programming Assignment #2
DESCRIPTION: This is the provided server.py script. It was modified to generate the print statements in the example
output section of the spec sheet. It listens on port 12000 of the local machine (Mininet Server) for UDP messages,
capitalizes received messages and replies to the client with the modified message. It "drops" packets by choosing
not to respond to messages chosen through the value of a randomly generated number within the interval of 0 to 10. It
displays output to the terminal window.
"""

# Server.py
# We will need the following module to generate
# randomized lost packets
import random
from socket import *

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(("127.0.0.1", 12000))
pingnum = 0
while True:
    # Count the pings received
    pingnum += 1
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the
    # address it is coming from
    message, address = serverSocket.recvfrom(1024)
    modifiedMessage = message.decode().upper()

    print("PING {0} Recieved".format(pingnum))
    print("Mesg rcvd: {0}".format(message.decode()))

    # If rand is less is than 4, and this not the
    # first "ping" of a group of 10, consider the
    # packet lost and do not respond

    if rand < 4 and pingnum % 10 != 1:
        print("Packet was lost.\n")
        continue

    # Otherwise, the server responds
    serverSocket.sendto(modifiedMessage.encode(), address)
    print("Mesg sent: {0}\n".format(modifiedMessage))
