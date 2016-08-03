#!/usr/bin/env python
# coding: utf8

from flask import Flask, jsonify, render_template, request
import RPi.GPIO as GPIO
import time

servo1PIN = 17
servo2PIN = 18
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo1PIN, GPIO.OUT)
GPIO.setup(servo2PIN, GPIO.OUT)

s1 = GPIO.PWM(servo1PIN, 50) # GPIO 17 als PWM mit 50Hz
s2 = GPIO.PWM(servo2PIN, 50) # GPIO 18 als PWM mit 50Hz
s1.start(7.5) # Initialisierung
s2.start(6.8)
time.sleep(0.8)
s1.ChangeDutyCycle(0)
s2.ChangeDutyCycle(0)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.php')

@app.route('/online/')
def online():
    ret_data = {"value": request.remote_addr}
    return jsonify(ret_data)

@app.route('/camera/', methods=['GET'])
def camera():
    ret_data = {"value": request.args.get('aktion')}
    wert = request.args.get('aktion')

    if(wert == "left"):
        s1.ChangeDutyCycle(13)

    elif(wert == "up"):
        s2.ChangeDutyCycle(2.5)


    elif(wert == "right"):
        s1.ChangeDutyCycle(2.9)

    elif(wert == "down"):
        s2.ChangeDutyCycle(13)

    elif(wert == "clear"):
        s1.ChangeDutyCycle(0)
        s2.ChangeDutyCycle(0)

    elif(wert == "reset"):
        s1.ChangeDutyCycle(7.5)
        s2.ChangeDutyCycle(6.8)

    elif(wert == "stop-camera-left" or wert == "stop-camera-right"):
        s1.ChangeDutyCycle(7.5)

    elif(wert == "stop-camera-up" or wert == "stop-camera-down"):
        s2.ChangeDutyCycle(6.8)


    else:
        print "Unbekannter Befehl: " + str(wert)

    return jsonify(ret_data)

def moveServo(x, y):
    s1.ChangeDutyCycle(x)
    s2.ChangeDutyCycle(y)

@app.route('/cameramove/', methods=['GET'])
def cameramove():
    ret_data = True
    x = float(request.args.get('x'))
    y = float(request.args.get('y'))
    moveServo(x, y)
    return jsonify(ret_data)

@app.route('/drive/', methods=['GET'])
def drive():
    ret_data = {"value": request.args.get('aktion')}
    wert = request.args.get('aktion')
    print wert
    return jsonify(ret_data)

@app.route('/sensors/', methods=['GET'])
def sensors():
    temp1 = 23.5
    temp2 = 21.2
    ret_data = {"temp1": temp1, "temp2": temp2}
    return jsonify(ret_data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False, threaded=True)
