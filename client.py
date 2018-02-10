from socket import *
serverName = "127.0.0.1"
serverPort = 12900

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = []
operator = raw_input("""Welcome to the Math Space!
    Select a number for the operation!
    (1) Addition  (2) Subtraction
    (3) Multiplication (4)Division   """)

message.append(operator)
operand1 = raw_input("Enter first number")
message.append(operand1)
operand2 = raw_input("Enter second number")
message.append(operand2)

message = ",".join(message)


clientSocket.sendto(message, (serverName, serverPort))

result, serverAddress = clientSocket.recvfrom(1024)
print "The answer is {0}".format(result)
clientSocket.close()
