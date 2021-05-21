"""
This is the framework for UDPClient, adapted from Assignment 1.

Note:
    Have not converted times to milliseconds.
    string.format() must be used instead of f-string literals for Python 3.5 (mininet)
"""

from socket import *        # Used to create sockets.
import timeit
serverName = "10.0.0.2"     # Sets name of server to hostname (DNS will provide IP of localhost)
serverPort = 12000          # Sends to arbitrary port number of 1200 (to avoid well known hosts)

# Functions for EMWA Calculations based on slides
def est_rtt(est_rtt, sample_rtt, alpha = 0.125):
    return (1 - alpha) * est_rtt + alpha * sample_rtt

def dev_rtt(dev_rtt, sample_rtt, est_rtt, beta = 0.25):
    return (1 - beta) * dev_rtt + beta * abs(sample_rtt - est_rtt)

def timeout_int(est_rtt,dev_rtt):
    return est_rtt + 4 * dev_rtt

# Functions for print formatting
def ms(seconds):
    """
    Conversion to milliseconds.
    :param seconds: Default output from timeit.
    :return: Float of milliseconds converted from seconds
    """
    return seconds * 1000

#Set initial values to 0 for testing
packets_lost = 0
sample_rtt = 0
total_rtt = 0
cur_est_rtt = 0
cur_dev_rtt = 0
curr_time_out = 1
min_rtt = max_rtt = 0

for pingnum in range(1,11):

    try:
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.settimeout(curr_time_out)
        message = "Ping{0}".format(pingnum)

        # Start timer & send msg to server
        start_time = timeit.default_timer()
        clientSocket.sendto(message.encode(),(serverName, serverPort))

        # Message sent (must be placed before timeout exception can occur)
        print("Mesg sent: {0}".format(message))

        # Receive msg from server abd stop timer
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        return_time = timeit.default_timer()

        # RTT calculations
        sample_rtt = return_time - start_time
        total_rtt += sample_rtt

        # Set initial values of est_rtt and dev_rtt after first successful RTT measurement
        if cur_est_rtt == 0:
            cur_est_rtt = sample_rtt
            cur_dev_rtt = sample_rtt / 2

        # EWMA Calucations & timeout
        cur_est_rtt = est_rtt(cur_est_rtt,sample_rtt)
        cur_dev_rtt = dev_rtt(cur_dev_rtt,sample_rtt,cur_est_rtt)
        curr_time_out = timeout_int(cur_est_rtt,cur_dev_rtt)

        # Set values of min and max rtt if values reach new minimum or maximum
        if min_rtt == 0 or sample_rtt < min_rtt:
            min_rtt = sample_rtt
        if max_rtt == 0 or sample_rtt > max_rtt:
            max_rtt = sample_rtt

        # Print statements below (Per loop stats)
        print("Mesg rcvd: {0}".format(modifiedMessage.decode()))
        print("Start time: {0}".format(start_time))
        print("Return time: {0}".format(return_time))
        print("Pong{0} RTT: {1} ms\n".format(pingnum, ms(sample_rtt)))

    except timeout:
        print("No Mesg rcvd")
        print("PONG{0} Request Timed out\n".format(pingnum))
        packets_lost += 1
    finally:
        clientSocket.close()

#Print statements below (end of run stats)
print("\nMin RTT: {0} ms".format(ms(min_rtt)))
print("Max Rtt: {0} ms".format(ms(max_rtt)))
print("Avg RTT: {0} ms".format(ms(total_rtt/(10-packets_lost))))
print("Packet Loss: {0}%".format((packets_lost/10) * 100))
print("Estimated RTT: {0} ms".format(ms(cur_est_rtt)))
print("Dev RTT: {0} ms".format(ms(cur_dev_rtt)))
print("Timeout Interval:{0} ms".format(ms(curr_time_out)))
