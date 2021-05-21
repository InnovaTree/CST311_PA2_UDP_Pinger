"""
This is the framework for UDPClient, adapted from Assignment 1.
"""

from socket import *        # Used to create sockets.
import timeit
serverName = "127.0.0.1"    # Sets name of server to hostname (DNS will provide IP of localhost)
serverPort = 12000          # Sends to arbitrary port number of 1200 (to avoid well known hosts)

#Set initial values to 0 for testing
sample_rtt = 0
cur_est_rtt = 0
cur_dev_rtt = 0
curr_time_out = 0
min_rtt = max_rtt = 0

for pingnum in range(1,11):

    """
    This sends 10 pings in a loop, starting at 1. There needs to be a timeout exception otherwise
    the program will freeze (block/wait for lost packet from server.
    """

    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Start timer & send msg to server
    start_time = timeit.default_timer()
    clientSocket.sendto(message.encode(),(serverName, serverPort))

    # Receive msg from server abd stop timer
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    return_time = timeit.default_timer() - start_time

    # Print statements below (Per loop stats)
    # Message sent
    # Message recvd
        # No Message Recieved
        # Timeout
    # Start Time
    # Return Time
    # RTT
    message = f"Ping{pingnum}"
    print(modifiedMessage.decode())
    clientSocket.close()

#Print statements below (end of run stats)
# Min RTT
# Max RTT
# Avg RTT
# Packet Loss %
# Estimated RTT
# Dev RTT
# Timeout Interval


