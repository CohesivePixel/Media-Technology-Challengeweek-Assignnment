import sys
import os
import time
import RPi.GPIO as GPIO
from autoOnClass import autoOnDef
from flask import Flask, render_template, request

app = Flask(__name__)

autoOnDef = autoOnDef()

StepPins = [17, 22, 23, 24]

autoOnState = 'false'


def Stappen(p):
    for i in range(0, 4):
        GPIO.output(StepPins[i], p[i])
    time.sleep(0.00125)


def up(max):
    for i in range(0, max):
        stopKnop = GPIO.input(20)
        if stopKnop == 0:
            return
        else:
            Stappen([1, 0, 0, 1])
            Stappen([0, 0, 0, 1])
            Stappen([0, 0, 1, 1])
            Stappen([0, 0, 1, 0])
            Stappen([0, 1, 1, 0])
            Stappen([0, 1, 0, 0])
            Stappen([1, 1, 0, 0])
            Stappen([1, 0, 0, 0])


def down(max):
    for i in range(0, max):
        Stappen([1, 0, 0, 0])
        Stappen([1, 1, 0, 0])
        Stappen([0, 1, 0, 0])
        Stappen([0, 1, 1, 0])
        Stappen([0, 0, 1, 0])
        Stappen([0, 0, 1, 1])
        Stappen([0, 0, 0, 1])
        Stappen([1, 0, 0, 1])


def stappenmotorserver(richting, max):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(StepPins[0], GPIO.OUT)
    GPIO.setup(StepPins[1], GPIO.OUT)
    GPIO.setup(StepPins[2], GPIO.OUT)
    GPIO.setup(StepPins[3], GPIO.OUT)
    GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    if richting == 'up':
        up(max)
        GPIO.cleanup()
    else:
        down(max)
        GPIO.cleanup()


def animatie():
    time.sleep(2)
    stappenmotorserver('down', 6)
    time.sleep(0.01)
    stappenmotorserver('up', 3000)
    time.sleep(0.01)
    stappenmotorserver('down', 1500)
    time.sleep(0.01)
    stappenmotorserver('up', 750)
    time.sleep(0.01)
    stappenmotorserver('down', 325)
    time.sleep(0.01)
    stappenmotorserver('up', 200)
    time.sleep(0.01)
    stappenmotorserver('down', 100)
    time.sleep(0.01)
    stappenmotorserver('up', 20000)


# animatie()

@app.route("/home.htm")
def home():
    global autoOnState
    if autoOnState == 'false':
        stappenmotorserver('up', 200000)
        return render_template('index.htm')
    else:
        return render_template('index.htm')


@app.route("/up.htm")
def omhoog():
    global autoOnState
    if autoOnState == 'false':
        steps = 1
        steps = int(request.args.get('steps'))
        stappenmotorserver('up', steps)
        return render_template('index.htm')
    else:
        return render_template('index.htm')


@app.route("/down.htm")
def omlaag():
    global autoOnState
    if autoOnState == 'false':
        steps = 1
        steps = int(request.args.get('steps'))
        stappenmotorserver('down', steps)
        return render_template('index.htm')
    else:
        return render_template('index.htm')


@app.route("/")
def hello():
    return render_template('index.htm')


@app.route("/reboot.htm")
def reboot():
    global autoOnState
    if autoOnState == 'false':
        os.system("sudo reboot")
        return render_template('index.htm')
    else:
        return render_template('index.htm')


@app.route("/shutdown.htm")
def shutdown():
    global autoOnState
    if autoOnState == 'false':
        os.system("sudo shutdown -h now")
        return render_template('index.htm')
    else:
        return render_template('index.htm')


@app.route("/xpos.htm")
def xpos():
    global autoOnState
    if autoOnState == 'false':
        file = open('/boot/xpos.txt', 'r')
        return file.read()
    else:
        return render_template('index.htm')


@app.route("/ypos.htm")
def ypos():
    global autoOnState
    if autoOnState == 'false':
        file = open('/boot/ypos.txt', 'r')
        return file.read()
    else:
        return render_template('index.htm')


@app.route("/auto_on.htm")
def autoOn():
    global autoOnState
    autoOnState = 'true'
    autoOnDef.autoOn = 'true'
    autoOnDef.autoOnOff()
    return render_template('index.htm')


@app.route("/auto_off.htm")
def autoOff():
    global autoOnState
    autoOnState = 'false'
    print("off")
    autoOnDef.autoOn = 'false'
    print(str(autoOnDef.autoOn))
    GPIO.cleanup()
    return render_template('index.htm')


@app.route("/SelfAnimatie")
def SelfAnimatie():
    animatie()
    # autoOnDef.animatie()
    return render_template('index.htm')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)
