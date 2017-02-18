#!/usr/bin/env python
#import modules
import sys
sys.path.append(&#8216;/home/pi/Adafruit-Raspberry-Pi-Python-Code/Adafruit_PWM_Servo_Driver&#8217;)
from Adafruit_PWM_Servo_Driver import PWM
import time
import os
import RPi.GPIO as GPIO
import pygame
#setup GPIO for LEDs
GPIO.setmode(GPIO.BCM)
RED_LED = 18
GREEN_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
def flash_led(color, delay, times):
	for i in range(times):
		GPIO.output(color, GPIO.HIGH)
		time.sleep(delay)
		GPIO.output(color, GPIO.LOW)
		time.sleep(delay)
#setup GPIO for LEDs
GPIO.setmode(GPIO.BCM)
GREEN_LED = 18
RED_LED = 23
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)
#flash red LED quickly 5 times
#start pygame
pygame.init()
# Wait for a joystick
while pygame.joystick.get_count() == 0:
	print &#8216;waiting for joystick count = %i&#8217; % pygame.joystick.get_count()
	flash_led(RED_LED, 1, 5) #replaced time.sleep(10) with 10 seconds of blinking
	pygame.joystick.quit()
	pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()
print &#8216;Initialized Joystick : %s&#8217; % j.get_name()
GPIO.output(GREEN_LED, GPIO.HIGH)
# Key mappings
PS3_BUTTON_START = 3
PS3_AXIS_LEFT_VERTICAL = 1
PS3_AXIS_RIGHT_VERTICAL = 3
PS3_AXIS_L2 = 12
PS3_AXIS_R2 = 13
PS3_AXIS_L1 = 14
PS3_AXIS_R1 = 15
PS3_AXIS_DPAD_UP = 8
PS3_AXIS_DPAD_RIGHT = 9
PS3_AXIS_DPAD_DOWN = 10
PS3_AXIS_DPAD_LEFT = 11
# PWM channels
SERVO_LEFT_DRIVE = 0
SERVO_RIGHT_DRIVE = 1
SERVO_GRIPPER_OPEN_CLOSE = 2
SERVO_GRIPPER_UP_DOWN = 3
#PWM ranges
SERVO_FULL_CW = 296
SERVO_STOP = 328
SERVO_FULL_CCW = 360
#pressing &#8220;Start&#8221; button will increment exitCount until exitCountMax, when program quits
exitCount = 0
exitCountMax = 5
def driveServo(channel, speed):
	#calculate PWM pulse (32 is the range between SERVO_STOP and SERVO_FULL)
	pulse = SERVO_STOP
	if speed != 0:
		pulse = (speed * 32) + SERVO_STOP
	#tell servo what to do
	pwm.setPWM(channel, 0, int(pulse))
	#tell user what we did
	#print &#8220;Speed %.3f Pulse %i&#8221; % (speed, pulse)
def processControl(event):
	global exitCount
	if event.type == pygame.JOYBUTTONDOWN:
		if event.button == PS3_BUTTON_START:
			exitCount += 1
			#print &#8220;Start (will quit program at %i): %i&#8221; % (exitCountMax, exitCount)
			flash_led(RED_LED, 0.2, exitCount) #display exitCount
	elif event.type == pygame.JOYAXISMOTION:
		if event.axis == PS3_AXIS_LEFT_VERTICAL:
			driveServo(SERVO_GRIPPER_OPEN_CLOSE, -event.value)
		elif event.axis == PS3_AXIS_RIGHT_VERTICAL:
			driveServo(SERVO_GRIPPER_UP_DOWN, event.value)
		elif event.axis == PS3_AXIS_L2:
			driveServo(SERVO_LEFT_DRIVE, event.value)
		elif event.axis == PS3_AXIS_L1:
			driveServo(SERVO_LEFT_DRIVE, -event.value)
		elif event.axis == PS3_AXIS_R2:
			driveServo(SERVO_RIGHT_DRIVE, -event.value)
		elif event.axis == PS3_AXIS_R1:
			driveServo(SERVO_RIGHT_DRIVE, event.value)
		elif event.axis == PS3_AXIS_DPAD_UP:
			driveServo(SERVO_LEFT_DRIVE, event.value)
			driveServo(SERVO_RIGHT_DRIVE, event.value)
		elif event.axis == PS3_AXIS_DPAD_DOWN:
			driveServo(SERVO_LEFT_DRIVE, -event.value)
			driveServo(SERVO_RIGHT_DRIVE, -event.value)
		elif event.axis == PS3_AXIS_DPAD_LEFT:
			driveServo(SERVO_LEFT_DRIVE, -event.value)
			driveServo(SERVO_RIGHT_DRIVE, event.value)
		elif event.axis == PS3_AXIS_DPAD_RIGHT:
			driveServo(SERVO_LEFT_DRIVE, event.value)
			driveServo(SERVO_RIGHT_DRIVE, -event.value)
# Initialise the PWM device using the default address
pwm = PWM(0x40, debug=True)
pwm.setPWMFreq(50)                        # Set frequency to 60 Hz
try:
    # Loop forwever
    while exitCount < exitCountMax:
        # Sleep so we don't eat up all the CPU time
        time.sleep(0.1)

        # read in events
        events = pygame.event.get()

        # and process them
        for event in events:
            processControl(event)


except KeyboardInterrupt:
    j.quit()
    GPIO.cleanup() #cleanup GPIO on KeyboardInterrupt exit

#cleanup GPIO on normal exit
GPIO.cleanup()
