# Documentation

Assets and class-provided requirements for this programming assigment are stored in this directory.

# Announcements

**All members complete this by Sun night, 5/16:**
Post in slack about your preferred work role if any. If there is no preference,
I will randomly assign roles.

# Contents

[Team Lead](#team-lead)

[Project Rundown](#project-rundown)

[Work Division](#work-division)

#Team Lead
Ian Rowe

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
- Get the program to run on Mininet

**What do we submit?**

- Client and server code ( **follow the naming convention** )
- Meeting minutes for all 3 meetings
- Screenshots of server &amp; client output (**in one pdf file)**
- &quot;Fill in columns B and C with RTTs and lost packets as indicated in the file - Output Checker. Your outputs in your screenshots must match the outputs calculated in the Output Checker.&quot;

One submission per team

[Return to Top](#contents)

# Work Division

[Return to Top](#contents)