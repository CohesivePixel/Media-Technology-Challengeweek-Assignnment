import time
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BCM)

StepPins = [17, 22, 23, 24]
StepAantal = 0

max = int(sys.argv[1])

while StepAantal < max:

    GPIO.setmode(GPIO.BCM)

    for pin in StepPins:
        print(StepAantal)
        print("Pins aan het setten")
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, True)
        time.sleep(0.01)
        GPIO.output(pin, False)
        StepAantal = StepAantal + 1
    GPIO.cleanup()
