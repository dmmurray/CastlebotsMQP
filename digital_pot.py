import sys
import time
import RPi.GPIO as GPIO

SPI_CS_PIN = 17
SPI_SDISDO_PIN = 22 # mosi
SPI_CLK_PIN = 23

def sleep(a = 0.1):
    time.sleep(a)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SPI_CS_PIN, GPIO.OUT)
GPIO.setup(SPI_CLK_PIN, GPIO.OUT)
GPIO.setup(SPI_SDISDO_PIN, GPIO.OUT)

GPIO.output(SPI_CLK_PIN, False)
GPIO.output(SPI_SDISDO_PIN, False)
GPIO.output(SPI_CS_PIN, False)

print "Setup"
GPIO.output(SPI_CS_PIN, True)
GPIO.output(SPI_CLK_PIN, False)
GPIO.output(SPI_CS_PIN, False)

def set_value(b):
    tmp = b # Remember parameter value
    b = "0000" "00" "{0:010b}".format(b)

    GPIO.output(SPI_CS_PIN, False)
    for x in b:
        GPIO.output(SPI_SDISDO_PIN, int(x))
        GPIO.output(SPI_CLK_PIN, True)
        #For step by step checking: sleep()
        GPIO.output(SPI_CLK_PIN, False)
        #For step by step checking: sleep()

    GPIO.output(SPI_CS_PIN, True)
    print "Digital pot set to %d" % tmp
    sleep()


def main():
    set_value(110)

#def _init_():
main()
    
