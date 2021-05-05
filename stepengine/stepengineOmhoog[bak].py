import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

StepPins = [24,23,22,17]
AantalSteps = 0

while True :

	GPIO.setmode(GPIO.BCM)	

	for pin in StepPins :
		print (AantalSteps)
		print ("PinsAanHetChecken")
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, True)
		time.sleep(0.01)
		GPIO.output(pin, False)
		AantalSteps = AantalSteps + 1
		
	GPIO.cleanup()
