import time
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True :
	
	a = GPIO.input(20)	

	if a != 1 :
		print("Stopt.....")
		sys.exit()
	
	time.sleep(0.1)
