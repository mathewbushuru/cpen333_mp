# Part 2
# Student 1
# Name:             Mathew Bushuru
# Student number:   81262800

# Student 2
# Name:
# Student number:


from socket import *
import time, random

serverPort = 12000

# Create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# bind socket to localport number 12000
serverSocket.bind(("", serverPort))
print("The server  is ready to receive")

while True:
    # read from UDP  socket into message,  getting client IP and port
    message, clientAddress = serverSocket.recvfrom(2048)
    # modify message
    receivedMessage = message.decode()
    modifiedMessage = receivedMessage[0:7] + " ditto"
    sleep_time = random.randint(5, 51) / 1000  # in seconds
    time.sleep(sleep_time)

    # generating a random integer between 1 and 100. The probability of a number being between 1 and 10 is 10%
    random_number = random.randint(1, 101)
    print("random no ", random_number)
    if random_number > 10:
        # send message back to client
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
