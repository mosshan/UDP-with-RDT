
from socket import *
import random

serverPort = 12419
serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('', serverPort))

print ('The server is ready to receive')

while True:
	message, clientAddress = serverSocket.recvfrom(6790)
	modifiedMessage = message.decode().upper()

	print(" ")
	print("connection from ", end=" ")
	print(clientAddress,end=" ")
	print(" message " + modifiedMessage[5], end=" ")

	randomFloat = random.random()
	if(randomFloat < 0.7):
		serverSocket.sendto(modifiedMessage.encode(), clientAddress)
