import Adafruit_PCA9685
#from pwm import PWM
import RPi.GPIO as GPIO
import time

pwm = Adafruit_PCA9685.PCA9685()
GPIO.setmode(GPIO.BCM)
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

def moveMotor(motor, value):
    print "Motor bewegt! ( Motor: " + str(motor) + " | Value: " + str(value) + " )"
    pwm.set_pwm(motor, 0, value)
    #pwm.setPWM(motor, 0, value)

def stopMotor(pin):
    if(pin == 1):
        GPIO.output(5, GPIO.LOW)
    if(pin == 2):
        GPIO.output(6, GPIO.LOW)
    if(pin == 3):
        GPIO.output(13, GPIO.LOW)
    if(pin == 4):
        GPIO.output(19, GPIO.LOW)

def stopAll():
    GPIO.output(5, GPIO.LOW)
    GPIO.output(6, GPIO.LOW)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)

def startMotor(pin, speed):
    if(pin == 1):
        GPIO.output(5, GPIO.HIGH)
        pwm.set_pwm(2, 0, speed)
    if(pin == 2):
        GPIO.output(6, GPIO.HIGH)
        pwm.set_pwm(2, 0, speed)
    if(pin == 3):
        GPIO.output(13, GPIO.HIGH)
        pwm.set_pwm(3, 0, speed)
    if(pin == 4):
        GPIO.output(19, GPIO.HIGH)
        pwm.set_pwm(3, 0, speed)
