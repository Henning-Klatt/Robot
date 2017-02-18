#!/usr/bin/python

import pygame
import sys

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

print "Joystics:", pygame.joystick.get_count()
print "ID:      ", j.get_id()
print "Name:    ", j.get_name()
print "Buttons: ", j.get_numbuttons()
print "Axis:    ", j.get_numaxes()
print "Numhats: ", j.get_numhats()
print "Numballs ", j.get_numballs()

try:

    while j.get_button(3) == 0:

        pygame.event.pump()
		speed= j.get_axis(13)
		pwmout= speed * 1023

		if j.get_axis(13) != 0.00:
			print int(pwmout)


		elif j.get_axis(13) == 0.00:
except KeyboardInterrupt:
	j.quit()
	sys.exit()
