import Adafruit_PCA9685
import time

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
pwm.set_pwm(0, 0, 300)
pwm.set_pwm(1, 0, 300)

def moveServo(x, y):
    print "Servo bewegt! ( x: " + str(x) + " | y: " + str(y) +" )"
    pwm.set_pwm(0, 0, x)
    pwm.set_pwm(1, 0, y)
