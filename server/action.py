#!/usr/bin/env python
# coding: utf8
import time
import serial

class Action:
    def moveServo(self, x, y):
        try:
            print "Servo bewegt! ( x: " + str(x) + " | y: " + str(y) +" )"
            self.arduino.write('1,1,' + str(x))
            time.sleep(0.1)
            self.arduino.write('2,1,' + str(y))
        except AttributeError:
            self.arduino = serial.Serial('/dev/ttyACM0', 9600)
            print "Arduino defined"
