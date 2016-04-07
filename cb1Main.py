import SocketServer
import Microphone

def main():
	socket1 = SocketServer('Castlebots1', 8080)
	mic1 = Microphone()
	socket1.connectSocket()
	mic1.read()
	mic1.getTime()
	# TODO: socket1.writeSocket(mic1.time, something.location)
	# TODO: put in threads
	# thread 1 will send commands to the arduino
	# thread 2 will get commands from the master and log them
