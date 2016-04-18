import SocketClient
import Microphone

def main():
	socket4 = SocketClient('Castlebots4', 8080)
	mic4 = Microphone()
	socket4.connectSocket()
	mic4.read()
	mic4.getTime()
	# TODO: socket1.writeSocket(mic1.time, something.location)
	# TODO: put in threads
	# thread 1 will send commands to the arduino
	# thread 2 will get commands from the master and log them
