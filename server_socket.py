import socket

s = socket.socket()
print('socker created')
s.bind(('localhost', 9999))
s.listen(3)
print('waiting for client connection')

while True:
	c, addr = s.accept()
	name = c.recv(1024).decode()
	print(f"connected with c {c} and addr {addr} and name is {name}")
	c.send(bytes('Weolcome to Server', 'utf-8'))
	c.close()



