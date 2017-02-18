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
    for i in range(0, j.get_numaxes()):
        axis[i] = j.get_axis(i)
    for i in range(0, j.get_numbuttons())
        button[i] = j.get_axis(i)
    print button[]
except KeyboardInterrupt:
	j.quit()
	sys.exit()
