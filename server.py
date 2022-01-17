import socket
import operator

# 'Converts' the string operator into a real operator
operators = { 
            "+": operator.add, 
            "-": operator.sub, '*' : operator.mul,
            '/' : operator.truediv,  
            '^' : operator.xor, 
            }

HOST = "192.168.0.2"
PORT = 12000

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind((HOST, PORT))

print('Server Iniciado')


messageBytes, address = socket.recvfrom(2048)
messageString = messageBytes.decode('utf-8')
print('Resultado =  {}'.format(messageString))

messageString = messageString.split(", ")
a = messageString[0]
b = messageString[1]
operator = messageString[2]

result = operators[operator](int(a), int(b))

socket.sendto(str(result).encode(), address)
