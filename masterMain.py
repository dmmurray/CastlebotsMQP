import SocketServer
import Trilaterator

def main():
	#threads
	socketMaster = SocketServer('master', 8080) #todo: add actual computer name
	socketMaster.connectSocket()
	socketMaster.readSocket()

	#create x, which is to be passed to the trilaterator

	result = Trilaterator.calculate(x)

	#if we have the bottom bots facing up and the top right bot facing left,
	# then we can move the bottom left bot forward then right, and the bottom
	# right bot and top left bot can go forward then left, no decision making
	# required (phase 1)


	#dummy variables
	goalx = 1
	goaly = 2

	x1pos = 0
	y1pos = 0
	
	x2pos = 3
	y2pos = 0
	
	x3pos = 3
	y3pos = 3


	# bottom left bot
	while (y1pos < goaly):
		moveForward(1)
		y1pos += 1

	turnRight()

	while (x1pos < goalx):
		moveForward(1)
		x1pos += 1


	#bottom right bot
	while (y2pos < goaly):
		moveForward(1)
		y2pos += 1

	turnLeft()

	while (x2pos > goalx):
		moveForward(1)
		x2pos -= 1


	#top right bot
	while (x3pos > goalx):
		moveForward(1)
		x3pos -= 1

	turnLeft()

	while (xy3pos > goaly):
		moveForward(1)
		x2pos -= 1
	