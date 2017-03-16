import Adafruit_PCA9685
import time
from __future__ import division

pwm = Adafruit_PCA9685.PCA9685()

servo_min = 150
servo_max = 600

def set_servo_pulse(channel, pulse):
    pulse_length = 1000000
    pulse_length //= 60
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm_freq(60)

while True:
    pwm.set_pwm(0, 0, servo_min)
    time.sleep(1)
    pwm.set_pwm(0, 0, servo_max)
    time.sleep(1)

def moveServo(x, y):
    print "Servo bewegt! ( x: " + str(x) + " | y: " + str(y) +" )"
    pwm.set_pwm(0, 0, x)
    pwm.set_pwm(1, 0, y)
