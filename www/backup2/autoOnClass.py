import sys
import os
import time
import RPi.GPIO as GPIO

class autoOnDef:
	def __init__(self):
		self.autoOn = 'false'
		self.StepPins = [17,22,23,24]
	
	def Stappen(self, p):
        	for i in range(0,4):
                	GPIO.output(self.StepPins[i],p[i])
        	time.sleep(0.00125)

	def stappenmotorserver(self, richting, max) :
		if self.autoOn == 'true':
        		GPIO.setmode(GPIO.BCM)
        		GPIO.setup(self.StepPins[0], GPIO.OUT)
        		GPIO.setup(self.StepPins[1], GPIO.OUT)
        		GPIO.setup(self.StepPins[2], GPIO.OUT)
        		GPIO.setup(self.StepPins[3], GPIO.OUT)
        		GPIO.setup(20, GPIO.IN, pull_up_down = GPIO.PUD_UP)

			if richting == 'up' :
                       		self.up(max)
                        	GPIO.cleanup()
                	else :
                        	self.down(max)
                        	GPIO.cleanup()


	def up(self, max) :
	        for i in range(0, max) :
        	        stopKnop = GPIO.input(20)
                	if stopKnop == 0 :
                        	return
                	else :
                        	self.Stappen([1,0,0,1])
                        	self.Stappen([0,0,0,1])
                        	self.Stappen([0,0,1,1])
                        	self.Stappen([0,0,1,0])
                        	self.Stappen([0,1,1,0])
                        	self.Stappen([0,1,0,0])
                        	self.Stappen([1,1,0,0])
                        	self.Stappen([1,0,0,0])

	def down(self, max) :
        	for i in range(0, max) :
        	        self.Stappen([1,0,0,0])
        	        self.Stappen([1,1,0,0])
        	        self.Stappen([0,1,0,0])
        	        self.Stappen([0,1,1,0])
        	        self.Stappen([0,0,1,0])
        	        self.Stappen([0,0,1,1])
        	        self.Stappen([0,0,0,1])
        	        self.Stappen([1,0,0,1])

	def timeout(self, amount):
		if self.autoOn == 'true':
			time.sleep(amount)

	def animatie(self) :
		GPIO.setmode(GPIO.BCM)
                while self.autoOn == 'true':
                	self.timeout(2)
                        self.stappenmotorserver('down', 1000)
                        self.timeout(1.2)
                      	self.stappenmotorserver('up', 800)
                        self.timeout(0.5)
                        self.stappenmotorserver('down', 700)
                        self.timeout(0.6)
                        self.stappenmotorserver('up', 500)
                        self.timeout(0.4)
                        self.stappenmotorserver('down', 400)
                        self.timeout(0.3)
                        self.stappenmotorserver('up', 200)
                        self.timeout(0.1)
                        self.stappenmotorserver('down', 100)
                        self.timeout(3)
			self.stappenmotorserver('up', 500)
			self.timeout(0.01)
			self.stappenmotorserver('down', 1500)
			self.timeout(1)
			self.stappenmotorserver('up', 750)
			self.timeout(10)
			self.stappenmotorserver('up', 20000)
			self.timeout(3)
			
	def check_light(self):
		while self.autoOn == "true" :
			GPIO.setmode(GPIO.BCM)
			GPIO.setup(25, GPIO.OUT)
			GPIO.output(25, False)
			GPIO.setup(13, GPIO.OUT)
                	time.sleep(0.1)
                	GPIO.setup(13, GPIO.IN)
                	if GPIO.input(13) > 0 :
				GPIO.output(25, True)
				self.animatie()
		

	def autoOnOff(self) :
		self.autoOn = 'true'
		self.check_light()

