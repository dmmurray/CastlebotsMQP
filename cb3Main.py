import SocketClient
import Microphone

def main():
	socket3 = SocketClient('Castlebots3', 8080)
	mic3 = Microphone()
	socket3.connectSocket()
	mic3.read()
	mic3.getTime()
	# TODO: socket1.writeSocket(mic1.time, something.location)
	# TODO: put in threads
	# thread 1 will send commands to the arduino
	# thread 2 will get commands from the master and log them
