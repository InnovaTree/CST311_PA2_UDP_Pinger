"""
This is the framework for UDPClient, adapted from Assignment 1.
"""

from socket import *        # Used to create sockets.
import timeit
serverName = "127.0.0.1"    # Sets name of server to hostname (DNS will provide IP of localhost)
serverPort = 12000          # Sends to arbitrary port number of 1200 (to avoid well known hosts)

def est_rtt(est_rtt, sample_rtt, alpha = 0.125):
    return (1 - alpha) * est_rtt + alpha * sample_rtt

def dev_rtt(dev_rtt, sample_rtt, est_rtt, beta = 0.25):
    return (1 - beta) * dev_rtt + beta * abs(sample_rtt - est_rtt)

def timeout_int(est_rtt,dev_rtt):
    return est_rtt + 4 * dev_rtt

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
        message = f"Ping{pingnum}"

        # Start timer & send msg to server
        start_time = timeit.default_timer()
        clientSocket.sendto(message.encode(),(serverName, serverPort))

        # Message sent (must be placed before timeout exception can occur)
        print(f"Mesg sent: \t\t{message}")

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
        print(f"Mesg rcvd: \t\t{modifiedMessage.decode()}")
        print(f"Start time: \t{start_time}")
        print(f"Return time: \t{return_time}")

        # RTT (if/else for formatting). Number of tabs changes when ping_num > 9
        if pingnum < 10:
            print(f"Pong{pingnum} RTT: \t\t{sample_rtt}\n")
        else:
            print(f"Pong{pingnum} RTT: \t{sample_rtt}\n")

    except timeout:
        print("No Mesg rcvd")
        print(f"PONG{pingnum} Request Timed out\n")
        packets_lost += 1
    finally:
        clientSocket.close()

#Print statements below (end of run stats)
# Min RTT
print(f"\nMin RTT:  \t\t{min_rtt}")
# Max RTT
print(f"Max Rtt:  \t\t{max_rtt}")
# Avg RTT
print(f"Avg RTT:  \t\t{total_rtt/(10-packets_lost)}")
# Packet Loss %
print(f"Packet Loss:  \t{(packets_lost/10) * 100}%")
# Estimated RTT
print(f"Estimated RTT: \t{cur_est_rtt}")
# Dev RTT
print(f"Dev RTT: \t\t{cur_dev_rtt}")
# Timeout Interval
print(f"Timeout Interval:{curr_time_out}")


