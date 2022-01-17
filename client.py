import socket

HOST = "192.168.0.2"
PORT = 12000


socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Digite o valor de A:')
a = input()

print('Digite o valor de B:')
b = input()

print('Digite a operação a ser realizada: ')
operator = input()

message = a +', '+b+', '+operator

socket.sendto(message.encode('utf-8'), (HOST, PORT))

data, address = socket.recvfrom(2048)
text = data.decode('utf-8')
print('Resultado = %s ' % (text) + "\n")

