import time
import RPi.GPIO as GPIO

a = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(22, GPIO.OUT)

while (a > 0): 
	GPIO.output(22, True)
	time.sleep(1)
	GPIO.output(22, False)
	time.sleep(1)
GPIO.cleanup()
