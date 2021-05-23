# Documentation

Assets and class-provided requirements for this programming assigment are stored in this directory.

# Announcements

All members, please use **Python 3** for this assignment. Mininet supports up to Python 3.5.

Meeting 2 has begun: from Sat 5/22 to Sun 5/23 evening.

<del>Meeting 2 (status check) will start on the weekend of **22-May** after the midterm. Good luck!</del>

<del>**All members complete this by Sun night, 5/16:**
Post in slack about your preferred work role if any. If there is no preference,
I will randomly assign roles.</del>

# Contents

1. [Team Lead](#team)
2. [Project Rundown](#project-rundown)
3. [Work Division](#work-division)
    - [Larry Chiem](#larry-chiem)
    - [Ian Rowe](#ian-rowe)
    - [Raymond Shum](#raymond-shum)
    - [Nicholas Stankovich](#nicholas-stankovich)

# Team
**LEAD: Ian Rowe**

MEMBERS: Larry Chiem, Raymond Shum, Nicholas Stankovich

[Return to Top](#contents)

# Project Rundown
**What are we doing?**

- We're creating a python script that sends a message to a server and receives a response.
- We're going to measure the amount of time it takes to send and receive a response. This is called Round-Trip Time (RTT).
- We're going to perform calculations using the RTT.

**How are we going to do this?**

- We're going to modify UDPClient.py from Project 1.
    - UDPClient already connects to a server, sends and receives a message.
- We're going to use Server.py (that was given to us in the project spec sheet).

**What is the program flow?**

- UDPClient connects to Server.py
- UDPClient sends and receives 10 messages in a loop.
- Server.py prints messages that it receives and sends.
- UDPClient calculates RTT for each message and prints the results individually.
    - If there is a timeout, then UDPClient prints that out, too.
- UDPClient prints summarized results from the ping test.

**What work needs to be done?**

- Modify UDPClient to form a UDP connection with Server.py.
- Confirm: UDPClient should send a message to Server.py. Server.py should capitalize the message and return it to UDPClient.
- Modify UDPClient to send 10 messages on a loop to Server.py.
- Implement timer (package) to record RTT.
- Calculate (**MUST BE PERFORMED WITHOUT USING LIST OR ARRAY)**:
    - Round-trip time (RTT)
    - Minimum RTT
    - Maximum RTT
    - Average RTT
    - Estimated RTT (equation in spec sheet)
    - Deviation RTT (equation in spec sheet)
    - Timeout Interval (equation in spec sheet)
    - Packet Loss percentage
- Modify Server.py and UDPClient so that they display print messages in the format shown in the spec sheet.
- Solution must be tested to confirm that calculations results must match the resultchecker spreadsheet.
- Get the program to run on Mininet:
    - Interpreter needs to be changed to use Python 3.4. 

**What do we submit? (ONE SUBMISSION PER TEAM)**

- Client and server code ( **follow the naming convention** )
- Meeting minutes for all 3 meetings
- Screenshots of server &amp; client output (**in one pdf file)**
- &quot;Fill in columns B and C with RTTs and lost packets as indicated in the file - Output Checker. Your outputs in your screenshots must match the outputs calculated in the Output Checker.&quot;
- All members fill out the peer review form but **do not submit screenshots**.

[Return to Top](#contents)

# Work Division

## Larry Chiem
> 1. Modify UDPClient.py to measure RTT per loop.
> 2. Modify UDPClient.py by creating if statement that checks for timeout if response time exceeds timeout interval.
> 3. Implement: this part of [Client Output.](https://github.com/InnovaTree/CST311_PA2_UDP_Pinger/blob/main/Documentation/Images/doc_client_output_p1.JPG)

[Return to Top](#contents)

## Ian Rowe

> 1. Modify UDPClient.py from PA#1 to connect with server.py.
> 2. Modify UDPClient.py to send 10 messages to server.py on a loop.
> 3. Implement: [Server Output.](https://github.com/InnovaTree/CST311_PA2_UDP_Pinger/blob/main/Documentation/Images/doc_server_output.jpg)

[Return to Top](#contents)

## Raymond Shum
> 1. Implement tracking for the following values:
>     - Minimum, Maximum, Average RTT, Packet Loss Percentage
> 2. Implement: this part of [Client Output.](https://github.com/InnovaTree/CST311_PA2_UDP_Pinger/blob/main/Documentation/Images/doc_client_output_p2.JPG)
> 3. Perform testing on Mininet using required test environment.
> 4. Confirm results on Output Checker spreadsheet.

[Return to Top](#contents)

## Nicholas Stankovich

> Create functions for calculations:
>  1. [Estimated RTT](https://github.com/InnovaTree/CST311_PA2_UDP_Pinger/blob/main/Documentation/Images/doc_est_rtt.jpg)
>  2. [Deviation RTT](https://github.com/InnovaTree/CST311_PA2_UDP_Pinger/blob/main/Documentation/Images/doc_dev_rtt.jpg)
>  3. [Timeout Interval](https://github.com/InnovaTree/CST311_PA2_UDP_Pinger/blob/main/Documentation/Images/doc_dev_rtt.jpg)

[Return to Top](#contents)
