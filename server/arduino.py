import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(200)
pwm.set_pwm(0, 0, 300)
pwm.set_pwm(1, 0, 300)

def moveServo(servo, value):
    print "Servo bewegt! ( Servo: " + str(servo) + " | Value: " + str(value) +" )"
    pwm.set_pwm(servo, 0, value)

def moveMotor(motor, value):
    print "Motor bewegt! ( Motor: " + str(motor) + " | Value: " + str(value) + " )"
    pwm.set_pwm(motor, 0, value)
