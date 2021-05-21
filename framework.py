"""
This is the framework for UDPClient, adapted from Assignment 1.
"""

from socket import *        # Used to create sockets.
import timeit
serverName = "127.0.0.1"    # Sets name of server to hostname (DNS will provide IP of localhost)
serverPort = 12000          # Sends to arbitrary port number of 1200 (to avoid well known hosts)

# Define functions for EMWA Calculations
# Initialize Variables here

for pingnum in range(1,11):
    """
    Loop needs to be performed in a try/catch/finally block. If packet is lost by server, then there will
    be a timeout exception.
    """
    try:
        clientSocket = socket(AF_INET, SOCK_DGRAM)

        # set clientSocket Timeout
        # Set message to be sent

        # Start Timer here
        # The message variable needs to be initialized before it can be sent
        clientSocket.sendto(message.encode(),(serverName, serverPort))

        # Print message for message sent to server

        # Receive msg from server
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        # Stop timer here

        # RTT calculations

        # Set initial values of est_rtt and dev_rtt after first successful RTT measurement

        # EWMA Calucations & timeout

        # Set values of min and max rtt if values reach new minimum or maximum

        # Print statements below (Per loop stats)

    except timeout:
        # Print timeout error messages
        # Track number of lost messages
        pass
    finally:
        clientSocket.close()
        pass

#Print statements below (end of run stats)


