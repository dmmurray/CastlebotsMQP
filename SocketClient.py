import socket

class SocketClient:

	def __init__(self, name, port):
		self.name = name
		self.port = port
		self.commands = []
		self.s = socket.socket()
	
	def connectSocket(self):
		self.s.connect((name, port))

	def readSocket(self):
		incoming = self.s.recv(1024)
		if (incoming):
			self.commands.append(incoming)

	def closeSocket(self):
		self.s.close()
