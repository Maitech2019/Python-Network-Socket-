#basic-client.py

import socket

server_ip = '192.168.1.156'
port = 7000

while True:
	data = input("Enter Message: ")
	server = socket.socket()
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

	server.connect((server_ip,port))
	server.send(data.encode('utf-8'))

	data_server = server.recv(1024).decode('utf-8')# max byt receive 1024 and decode to send in Thai utf-8
	print('Data from server: ', data_server)
	server.close()