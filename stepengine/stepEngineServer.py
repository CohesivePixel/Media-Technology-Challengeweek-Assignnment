# importeren bibliotheken
import time
import RPi.GPIO as GPIO
import sys

# instellen modus van GPIO
GPIO.setmode(GPIO.BCM)

# Definieren StepPins
StepPins = [17, 22, 23, 24]
Aantal = 512


# aanmaken def
def StepEngineServer(richting, max):
    # Definieren teller
    AantalSteps = 0
    pins = [17, 22, 23, 24]
    # if-statement om richting te bepalen
    if richting == 'up':
        pins.reverse()
        print("Up")
        print(pins)
    else:
        print("Down")
        print(pins)

    # de buitenste while loop. Stopt wanneer de teller het vooraf aangegeven aantal bereikt
    while AantalSteps < max:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        # elke pin in de lijst StepPins wordt nagelopen, aangezet, 0.002 seconden aan gelaten en uitgezet
        # daarna wordt bij de teller bijgeteld
        for pin in pins:
            # print AantalSteps
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, True)
            time.sleep(0.002)
            GPIO.output(pin, False)
            AantalSteps = AantalSteps + 1

            # stopt wanneer de stopknop ingedrukt wordt EN de richting 'up' is
            stopKnop = GPIO.input(20)
        if stopKnop == 0 and richting == 'up':
            print("Stopt...")
            break
        elif stopKnop == 0 and richting == 'down':
            print("Gaat weer omlaag")

        GPIO.cleanup()


# De Animatie
def animatie():
    time.sleep(2)
    StepEngineServer('down', 6000)
    time.sleep(0.01)
    StepEngineServer('up', 3000)
    time.sleep(0.01)
    StepEngineServer('down', 1500)
    time.sleep(0.01)
    StepEngineServer('up', 750)
    time.sleep(0.01)
    StepEngineServer('down', 325)
    time.sleep(0.01)
    StepEngineServer('up', 200)
    time.sleep(0.01)
    StepEngineServer('down', 100)
    time.sleep(5)
    StepEngineServer('up', 20000)


animatie()
