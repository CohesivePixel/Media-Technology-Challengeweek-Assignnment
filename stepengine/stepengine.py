#imports van bibliotheek
import time
import sys
import RPi.GPIO as GPIO

def stepengine(richtingF, maxF) :

	#declareren van richtingteller
	z = 2
	
	#set modus van GPIO
	GPIO.setmode(GPIO.BCM)

	#argumenten die meegegeven worden aan Stepengine.py
	max = maxF
	richting = richtingF

	#aangeven welke pinnen gebruikt moeten worden
	StepPins = [17,22,23,24]

	#declareren van teller
	AantalSteps = 0
	
	#delcareren van aantal argumenten
	AantalArgs = 1

	#declareren van teller argument
	teller = 1

	#if statement dat eerste richting bepaalt, stopt wanneer de input iets anders
	#dan 'up' of 'down' is
	if richting == 'down' :
		print("Omlaag")
	elif richting == 'up' :
		StepPins.reverse()
		print("Omhoog")
	else :
		print("Geen richting, stopt...")
		sys.exit()

	while teller <= AantalArgs :
	
		max = maxF
	
		#maximale aantal rondes van stappenmotor aangeven
		while AantalSteps < max :
		
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)	
			#gaat elke pin langs, zet deze aan, wacht 0.01sec en zet deze 
			#vervolgens weer uit, gaat naar de volgende pin
	
			#elke ronde wordt geteld
			for pin in StepPins :
				print ("Pins aan het setten")
				print(AantalSteps)
				GPIO.setup(pin, GPIO.OUT)
				GPIO.output(pin, True)
				time.sleep(0.002)
				GPIO.output(pin, False)
				AantalSteps = AantalSteps + 1
			
				#checkt constant of stopknop ingedrukt wordt
				#als knop ingedrukt wordt en richting 'up' is
				#wordt programma gestopt
				stopKnop = GPIO.input(20)

				if stopKnop == 0 and richting == 'up'  :
					print("Stopt...")
					sys.exit()
				elif stopKnop == 0 and richting == 'down' :
					print("gaat nogsteeds omlaag")
				
			GPIO.cleanup()				

		#telt 1 bij teller voor buitenste loop op en reset teller binnenste
		#loop, zorgt ook dat volgende argument uitgelezen wordt
		teller = teller + 1
		StepPins.reverse()
		AantalSteps = 0
		z = z + 1
		if richting == 'down' :
			richting = '
	
	return	

 	
stepengine('up', 300)
