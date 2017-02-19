import serial
import time

try:
    print "Arduino definiert"
    arduino = serial.Serial('/dev/ttyACM0', 57600)
except:
    print "Arduino definiert"
    arduino = serial.Serial('/dev/ttyACM1', 57600)

def moveServo(x, y):
    print "Servo bewegt! ( x: " + str(x) + " | y: " + str(y) +" )"
    arduino.write('1,1,' + str(x))
    time.sleep(.1)
    arduino.write('2,1,' + str(y))