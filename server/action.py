#!/usr/bin/env python
# coding: utf8

import serial
class Action:
    def __init__(self):
        try:
            arduino = serial.Serial('/dev/ttyACM0', 9600)
        except:
            arduino = serial.Serial('/dev/ttyACM1', 9600)

    def moveServo(x, y):
        print "Servo bewegt! ( x: " + str(x) + " | y: " + str(y) +" )"
        arduino.write('1,1,' + str(x))
        time.sleep(0.1)
        arduino.write('2,1,' + str(y))
