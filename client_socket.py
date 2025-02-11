import socket

c = socket.socket()
print('client socket created')

c.connect(('localhost', 9999))

name = input('Enter the name')

c.send(bytes(name, 'utf8'))

print(c.recv(1024).decode())
