from socket import *
import math
serverPort = 12900

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print "server is now running press ctrl c to stop it"



Addition= 1
Subtraction= 2
Modulus= 3
Division= 4
Power = 5

def MathOperation(message):

    message = message.split(",")
    operator = int(message[0])
    operand1= int(message[1])
    operand2= int(message[2])

    if (operator == Addition):
        return operand1 + operand2
    elif (operator == Subtraction):
        return operand2 - operand1
    elif (operator == Modulus):
        return operand1 % operand2
    elif (operator == Division):
        return operand1 / operand2
    elif (operator == Power):
        return math.pow(operand1, operand2)
    else:
        return "invalid operation"

while True:
    message, clientAddress = serverSocket.recvfrom(1024)
    response = str(MathOperation(message))
    print "sending response of operation"
    serverSocket.sendto(response, clientAddress)
