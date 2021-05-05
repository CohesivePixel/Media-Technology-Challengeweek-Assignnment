import time
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)

StepPins = [17,22,23,24]
AantalSteps = 0

StepPins.reverse()

max = int(sys.argv[1])

while AantalSteps < max :

	GPIO.setmode(GPIO.BCM)	

	for pin in StepPins :
		print (AantalSteps)
		print ("PinsAanHetChecken")
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, True)
		time.sleep(0.002)
		GPIO.output(pin, False)
		AantalSteps = AantalSteps + 1
		
	GPIO.cleanup()
