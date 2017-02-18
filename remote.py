#!/usr/bin/python

import pygame
import sys
import os
#pygame.init()
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

axes = [ 0.0 ] * j.get_numaxes()
buttons = [ False ] * j.get_numbuttons()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_alive = False
        elif event.type == pygame.JOYAXISMOTION:
            e = event.dict
            axes[e['axis']] = e['value']
        elif event.type in [pygame.JOYBUTTONUP, pygame.JOYBUTTONDOWN ]:
            e = event.dict
            buttons[e['button']] ^= True
        clock.tick(10)
