#!/usr/bin/python

import pygame
import sys

pygame.init()
clock = pygame.time.Clock()
j = pygame.joystick.Joystick(0)
j.init()

print "Joystics:", pygame.joystick.get_count()
print "ID:      ", j.get_id()
print "Name:    ", j.get_name()
print "Buttons: ", j.get_numbuttons()
print "Axis:    ", j.get_numaxes()
print "Numhats: ", j.get_numhats()
print "Numballs ", j.get_numballs()
axis = [0]*j.get_numaxes()
button = [0]*j.get_numbuttons()

def get_axis():
    pygame.event.pump()
    for i in range(0, j.get_numaxes()):
        axis[i] = j.get_axis(i)
    return axis

def get_buttons():
    pygame.event.pump()
    for i in range(0, j.get_numbuttons()):
        button[i] = j.get_axis(i)
    return button

try:
    while 1:
        print '[%s]' % ', '.join(map(str, get_axis()))
except KeyboardInterrupt:
	j.quit()
	sys.exit()
