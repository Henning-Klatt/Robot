import Adafruit_PCA9685
#from pwm import PWM
import RPi.GPIO as GPIO
import time

pwm = Adafruit_PCA9685.PCA9685()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.OUT)#M1 Links
GPIO.setup(6, GPIO.OUT)#M1 Rechts
GPIO.setup(13, GPIO.OUT)#M2 Links
GPIO.setup(19, GPIO.OUT)#M2 Rechts
#pwm = PWM(0x40)
#pwm.setPWMFreq(200)
pwm.set_pwm_freq(60)
pwm.set_pwm(0, 0, 300)
pwm.set_pwm(1, 0, 300)

def moveServo(servo, value):
    print "Servo bewegt! ( Servo: " + str(servo) + " | Value: " + str(value) +" )"
    pwm.set_pwm(servo, 0, value)

def stopMotor(pin):
    if(pin == 1):
        GPIO.output(5, GPIO.LOW)
        print "5 Low"
    if(pin == 2):
        GPIO.output(6, GPIO.LOW)
        print "6 Low"
    if(pin == 3):
        GPIO.output(13, GPIO.LOW)
        print "13 Low"
    if(pin == 4):
        GPIO.output(19, GPIO.LOW)
        print "19 Low"

def stopAll():
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)

def startMotor(pin, speed):
    if(pin == 1):
        GPIO.output(6, GPIO.LOW)
        GPIO.output(5, GPIO.HIGH)
        print "5 High"
        pwm.set_pwm(2, 0, speed)
    if(pin == 2):
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.HIGH)
        print "6 High"
        pwm.set_pwm(2, 0, speed)
    if(pin == 3):
        GPIO.output(19, GPIO.LOW)
        GPIO.output(13, GPIO.HIGH)
        print "13 High"
        pwm.set_pwm(3, 0, speed)
    if(pin == 4):
        GPIO.output(13, GPIO.LOW)
        GPIO.output(19, GPIO.HIGH)
        print "19 High"
        pwm.set_pwm(3, 0, speed)
