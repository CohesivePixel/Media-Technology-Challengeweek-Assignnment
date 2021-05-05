import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

def lichtsensor(pin) :
	lichtmeting = 0
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	time.sleep(0.1)
	
	GPIO.setup(pin, GPIO.IN)
	while(GPIO.input(pin) == GPIO.LOW) :
		lichtmeting = lichtmeting + 1
	return lichtmeting

print(lichtsensor(33))
