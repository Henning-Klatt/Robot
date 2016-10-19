#!/usr/bin/env python
# coding: utf8

from flask import Flask, jsonify, render_template, request
import RPi.GPIO as GPIO
import time, sys, os
import commands

servo1PIN = 17
servo2PIN = 4
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
def all():
    temp1 = 23.5
    temp2 = 21.2
    ip = request.remote_addr
    callback = request.args.get('callback')
    return '{0}({1})'.format(callback, {'client_ip':ip,'b':2,'temp1':temp1,'temp2':temp2})

@app.route('/online/')
def online():
    callback = request.args.get('callback')
    return '{0}({1})'.format(callback, {'online':'true'})

@app.route('/status/')
def status():
    callback = request.args.get('callback')
    statusfrom = request.args.get('from')
    if(statusfrom == "stream"):
        response = commands.getstatusoutput('sudo service motion status')
        print response
        if("Active: active (running)" in response):
            print "Camera Stream ist online!"
            return '{0}({1})'.format(callback, {'online':'true'})
        else:
            print "Camera Stream ist offline!"
            return '{0}({1})'.format(callback, {'online':'false'})



@app.route('/action/')
def action():
    callback = request.args.get('callback')
    action = request.args.get('action')
    if(action == "stopScript"):
        callback = request.args.get('callback')
        s1.ChangeDutyCycle(0)
        s2.ChangeDutyCycle(0)
        GPIO.cleanup()
        os.system("sudo pkill -9 python")
        return '{0}({1})'.format(callback, {'online':'true'})

    elif(action == "startStream"):
        callback = request.args.get('callback')
        os.system("sudo service motion start")
        print ("Camera Stream gestartet!")
        return '{0}({1})'.format(callback, {'streamstatus':'online'})

    elif(action == "stopStream"):
        callback = request.args.get('callback')
        os.system("sudo service motion stop")
        print ("camera Stream gestoppt")
        return '{0}({1})'.format(callback, {'streamstatus':'offline'})

    else:
        return '{0}({1})'.format(callback, {'Unbekannter Befehl!'})


def moveServo(x, y):
    print str(x)
    print str(y)

@app.route('/cameramove/', methods=['GET'])
def cameramove():
    callback = request.args.get('callback')
    x = request.args.get('x')
    y = request.args.get('y')
    moveServo(x, y)
    return '{0}({1})'.format(callback, {'success'})

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
    app.run(host='0.0.0.0', port=8081, debug=True, threaded=True)
