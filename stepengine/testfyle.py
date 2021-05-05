import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)


while True :
	GPIO.setup(33, GPIO.OUT)
	time.sleep(0.1)
	GPIO.setup(33, GPIO.IN)
	print(GPIO.input(33))
	if GPIO.input(33) == 0:
		print("Say Hi")
	else :
		print("hij doet t niet")
	time.sleep(0.1)
