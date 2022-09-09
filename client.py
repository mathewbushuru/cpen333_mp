# Part 2
# Student 1
# Name:             Mathew Bushuru
# Student number:  

# Student 2
# Name:
# Student number:

from socket import *
import time, random

serverName = "localhost"
# serverName = "127.0.0.1"
serverPort = 12000

# create udp socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)

for message_number in range(5):

    # keyboard input from user
    message = "PING " + str(message_number) + " - hello world"

    time_before = time.time()

    try:
        # attach server port and name to message and send into socket
        clientSocket.settimeout(1)
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        time_after = time.time()
        round_trip_time = time_after - time_before
        print(modifiedMessage.decode())
        print("ROUND TRIP TIME: ", round_trip_time * 1000, "ms \n")
    except timeout:
        print("Request timed out")
        time_after = time.time()
        round_trip_time = time_after - time_before
        print("ROUND TRIP TIME: ", round_trip_time * 1000, "ms \n")


clientSocket.close()
