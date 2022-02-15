#basic-server.py

import socket

server_ip = '192.168.1.156' #or ip
port= 7000

while True:
	server = socket.socket() #creat a socket
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1) #set option so socket to reuse same port

	server.bind((server_ip,port))
	server.listen(5) #backlog maximum receive incoming

	print('Waiting for client...')

	client, addr = server.accept()
	print("Connect from: ", str(addr))
	data = client.recv(1024).decode("utf-8") #number of byte can receive from client
	print("Message from client: ", data)
	client.send('We received your Message!'.encode('utf-8')) #before sending to client must encode too
	client.close()

