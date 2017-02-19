import serial
import time

if('arduino' in vars()):
    print "Arduino bereits definiert"
else:
    try:
        arduino = serial.Serial('/dev/ttyACM0', 57600)
        print "Arduino definiert auf /dev/ttyACM0"
    except Exception as e:
        print e
        arduino = serial.Serial('/dev/ttyACM1', 57600)
        print "Arduino definiert auf /dev/ttyACM1"

def moveServo(x, y):
    print "Servo bewegt! ( x: " + str(x) + " | y: " + str(y) +" )"
    arduino.write('1,1,' + str(x))
    time.sleep(.03)
    arduino.write('2,1,' + str(y))
