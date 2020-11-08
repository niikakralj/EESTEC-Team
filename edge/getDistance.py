import time
import random
import OPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setboard(GPIO.ZERO)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(8,GPIO.IN)

def getDistance():
    GPIO.setwarnings(False)
    GPIO.setboard(GPIO.ZERO)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7,GPIO.OUT)
    GPIO.setup(8,GPIO.IN)
    time1=int(round(time.time() * 1000))
    GPIO.output(7, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(7, GPIO.LOW)

#    while GPIO.input(8) is 0:
#        pass

    dt=int(round(time.time() * 1000))-time1

    return random.randint(1,100)