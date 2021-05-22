"""
This is the framework for UDPClient, adapted from Assignment 1.

Note:
    This is confirmed working and has been tested on Mininet.
    string.format() must be used instead of f-string literals for Python 3.5 (mininet)

To be done:
    Clean up variable initializations (optional).
    
    Confirm with Dr. Satyavolu or Millan: 
    
        Should initial time out be set to 1 second or 1 minute?
        
        Are we updating the actual timeout value of the socket with the calculated time
        out per loop or does it remain at 1 sec/min?
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

# Variables are initialized below:
packets_lost = 0            # Number of time outs in the entire run
sample_rtt = 0              # Measured RTT for current ping
total_rtt = 0               # Sum of all sample_rtt in the run
cur_est_rtt = 0             # Currently calculated est_rtt
cur_dev_rtt = 0             # Currently calculated dev_rtt
curr_time_out = 1           # Time out interval value, set to 1 second intially
min_rtt = max_rtt = 0       # Min and Max recorded rtt values in the run

# Loop will run 10 times, starting at 1 and ending at 10
for pingnum in range(1,11):

    # Program executes until a timeout exception is thrown.
    # Exception thrown if clientSocket exceeds timeout interval value.
    try:
        # Create a new socket, using IPv4, UDP and set current timeout value.
        clientSocket = socket(AF_INET, SOCK_DGRAM)
        clientSocket.settimeout(curr_time_out)
        
        # Create message to be sent as Ping[Loop#]
        message = "Ping{0}".format(pingnum)

        # Start timer & send msg to server.py
        start_time = timeit.default_timer()
        clientSocket.sendto(message.encode(),(serverName, serverPort))

        # Display message sent to terminal.
        # Must be placed here so it will run before timeout can occur.
        print("Mesg sent: {0}".format(message))

        # Receive msg from server and stop timer
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        return_time = timeit.default_timer()

        # Calculate sample RTT of current loop and add value to total RTT
        sample_rtt = return_time - start_time
        total_rtt += sample_rtt
        
        # Set new min/max RTT if new sample RTT is lower or higher than the currently recorded values
        if min_rtt == 0 or sample_rtt < min_rtt:
            min_rtt = sample_rtt
        if max_rtt == 0 or sample_rtt > max_rtt:
            max_rtt = sample_rtt

        # Set initial values of est_rtt and dev_rtt after first successful RTT measurement
        # This is only to set the initial values for calculations in the first loop.
        if cur_est_rtt == 0:
            cur_est_rtt = sample_rtt
            cur_dev_rtt = sample_rtt / 2

        # Perform EWMA Timeout Interval calculations, updating current values.
        # The current dev/est rtt is passed into the functions along with the current sample rtt
        # to generate the new values.
        cur_est_rtt = est_rtt(cur_est_rtt,sample_rtt)
        cur_dev_rtt = dev_rtt(cur_dev_rtt,sample_rtt,cur_est_rtt)
        curr_time_out = timeout_int(cur_est_rtt,cur_dev_rtt)



        # Print statements below (Per loop stats)
        print("Mesg rcvd: {0}".format(modifiedMessage.decode()))
        print("Start time: {0}".format(start_time))
        print("Return time: {0}".format(return_time))
        print("Pong{0} RTT: {1} ms\n".format(pingnum, ms(sample_rtt)))

    except timeout:
        # timeout occurs if message is not received from server within the duration 
        # of the current timeout interval.
        print("No Mesg rcvd")
        print("PONG{0} Request Timed out\n".format(pingnum))
        packets_lost += 1
    finally:
        # clientSocket is closed at end of loop whether or not timeout occurs.
        clientSocket.close()

#Print statements below (end of run stats):
print("\nMin RTT: \t{0} ms".format(ms(min_rtt)))
print("Max Rtt: \t{0} ms".format(ms(max_rtt)))
print("Avg RTT: \t{0} ms".format(ms(total_rtt/(10-packets_lost))))
print("Packet Loss: \t{0}%".format((packets_lost/10) * 100))
print("Estimated RTT: \t{0} ms".format(ms(cur_est_rtt)))
print("Dev RTT: \t{0} ms".format(ms(cur_dev_rtt)))
print("Timeout Interval:{0} ms".format(ms(curr_time_out)))
