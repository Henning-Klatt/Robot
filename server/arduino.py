from pwm import PWM
import time

pwm = PWM(0x40)
pwm.setPWMFreq(60)#Servo: 60 | DC Motor: 200

def moveServo(servo, value):
    print "Servo bewegt! ( Servo: " + str(servo) + " | Value: " + str(value) +" )"
    pwm.setPWM(servo, 0, value)
    #pwm.set_pwm(servo, 0, value)

def moveMotor(motor, value):
    print "Motor bewegt! ( Motor: " + str(motor) + " | Value: " + str(value) + " )"
    #pwm.set_pwm(motor, 0, value)
    pwm.setPWM(motor, 0, value)
