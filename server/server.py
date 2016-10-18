#!/usr/bin/env python
# coding: utf8

from flask import Flask, jsonify, render_template, request
import RPi.GPIO as GPIO
import time, sys, os

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
        os.system("mkdir /tmp/stream")
        os.system("raspistill --nopreview -w 640 -h 480 -q 5 -o /tmp/stream/pic.jpg -tl 100 -th 0:0:0 &")
        os.system("LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i 'input_file.so -f /tmp/stream -n pic.jpg' -o 'output_http.so -w /usr/local/www'")
        print ("Camera Stream gestartet!")
        return '{0}({1})'.format(callback, {'stream':'online'})

    elif(action == "stopStream"):
        callback = request.args.get('callback')
        os.system("sudo pkill -9 raspistill")
        print ("camera Stream gestoppt")
        return '{0}({1})'.format(callback, {'stream':'offline'})

    else:
        return '{0}({1})'.format(callback, {'Unbekannter Befehl!'})


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
    app.run(host='0.0.0.0', port=8081, debug=False, threaded=True)
