#!/usr/bin/env python
# coding: utf8
import time
import serial

class Action:
    def moveServo(self, arduino, x, y):
        print "Servo bewegt! ( x: " + str(x) + " | y: " + str(y) +" )"
        arduino.write('1,1,' + str(x))
        time.sleep(0.1)
        arduino.write('2,1,' + str(y))
