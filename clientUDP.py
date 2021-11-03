#!/usr/bin/python           # This is client.py file

from socket import *
from datetime import datetime
import sys

serverName = ''
serverPort = 12419
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)
#clientSocket.setTim
rtt_sum = 0.0;
timeout = 1.000;
numPacketsLost = 0
numPacketsRetransmitted = 0
for i in range(1, 11):
    modifiedMessage = None
    rtt_start = datetime.now()
    message = "Ping " + str(i) + " " + rtt_start.strftime("%Y-%m-%d %H:%M:%S%f")
    #clientSocket.sendto(message.encode(), (serverName, serverPort))
    print(message)


    #retransmit 3 times
    for j in range(0, 2):
        #wait until we have recieved a message?
        #while(float(datetime.timestamp(datetime.now()) - datetime.timestamp(rtt_start)) < timeout):
        try:
            clientSocket.sendto(message.encode(), (serverName, serverPort))
            modifiedMessage, serverAddress = clientSocket.recvfrom(6790)
            #if(modifiedMessage != None):
                #break
        except:
            print("Request timed out")
            if(j == 0):
                numPacketsRetransmitted += 1
            if(j == 2):
                numPacketsLost += 1
                break
            print("Packet retransmitted")
            continue
        if(modifiedMessage != None):
            break

    if(modifiedMessage != None):
        rtt_end = datetime.timestamp(datetime.now())
        rtt = rtt_end - datetime.timestamp(rtt_start)
        if(i == 1):
            min_rtt = rtt
            max_rtt = rtt
            rtt_sum = rtt
        else:
            if(rtt > max_rtt):
                max_rtt = rtt
            if(rtt < min_rtt):
                min_rtt = rtt
            rtt_sum += rtt
        print("server resp: " + modifiedMessage.decode())
    print()
    #if(datetime.now() - rtt_start > timeout):
        #retransmit
        #print("Retransmi")
    #modifiedMessage, serverAddress = clientSocket.recvfrom(6790)


avg_rtt = rtt_sum/10.0;
print()
print("Maximum RTT = ", max_rtt)
print("Minimum RTT = ", min_rtt)
print("Average RTT = ", avg_rtt)
print("Packet lost percentage = ", numPacketsLost/10.00)
print("Packets retransmitted = ", numPacketsRetransmitted)
clientSocket.close()
