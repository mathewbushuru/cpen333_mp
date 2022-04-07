# Part 2
from socket import *

serverName = "localhost"
serverPort = 12000

# create udp socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

# keyboard input from user
message = input("Input lowercase sentence:")

# attach server port and name to message and send into socket
clientSocket.sendto(message.encode(), (serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# print out received message
print(modifiedMessage.decode())

clientSocket.close()
