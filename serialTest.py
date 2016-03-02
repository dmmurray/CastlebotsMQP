import serial
import time
if __name__ == "__main__":
    print "Hello"
    ser = serial.Serial('/dev/ttyACM0', 9600)
    print "It's me"
    ser.write('100')
    print "I was lbiajs"
    x = 0
    print x
    #B = 0
    while x < 100:
        print "Starting..."
        ser.write('Connected?\n')
        con = ser.readline()
        print "con = " + str(con)
        if (x == 0):
            print "Gets in here"
            if (con == 'Connected'):
                ser.write('F')
                print "Sent F"
        if (con == 'Connected'):
            print con
        srl = ser.readline()
        if (srl == 'Finished forward'):
            #if (B == 1):
            #print "B = 1"
            ser.write('B')
            print "Sent B"
            #B = 0
        elif (srl == 'Finished backward'):
            #else:
            #print "B = 0"
            ser.write('F')
            print "Sent F"
            #B = 1
            #ser.write('100')
        print "x = " + str(x)
        #y = ser.readline()
        #print "y = " + y
        x += 1
        print "Hello from the Otter Slide"
        #time.sleep(4)
