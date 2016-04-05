import socket

class SocketServer:

	def __init__(self, name, port):
		self.name = name
		self.port = port
		self.s = socket.socket()
		self.c
	
	def connectSocket(self):
		self.s.bind((name, port))

	def readSocket(self):
		self.c, addr = self.s.accept()
		print('Got connection from', addr)
		self.c.send('Thank you for connecting')
		#self.c.close()
		#TODO: find out if this actually works too

	def writeSocket(self, content):
		self.c.send(content)
		#TODO: find out if this actually works

	def closeSocket(self):
		self.c.close()
		self.s.close()
