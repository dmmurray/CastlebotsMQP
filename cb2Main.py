import SocketServer
import Microphone

def main():
	socket2 = SocketServer('Castlebots2', 8080)
	mic2 = Microphone()
	socket2.connectSocket()
	mic2.read()
	mic2.getTime()
	# TODO: socket1.writeSocket(mic1.time, something.location)
	# TODO: put in threads
	# thread 1 will send commands to the arduino
	# thread 2 will get commands from the master and log them
