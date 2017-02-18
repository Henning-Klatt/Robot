#!/usr/bin/python
import pygame
import sys

pygame.init()
print "Joystics: ", pygame.joystick.get_count()
j = pygame.joystick.Joystick(0)
j.init()
print "ID: ", j.get_id()
print "Name: ", j.get_name()
print "Buttons: ", j.get_numbuttons()
print "Axis:    ", j.get_numaxes()
print "Numhats: ", j.get_numhats()
print "Numballs ", j.get_numballs()
clock = pygame.time.Clock()

select = 0
laxis = 1
raxis = 2
start = 3
lup = 4
lright = 5
ldown = 6
lleft = 7
l2 = 8
r2 = 9
l1 = 10
r1 = 11
rup = 12
rright = 13
rdown = 14
rleft = 15
ps = 16

try:
    while 1:
        for event in pygame.event.get():
            print "Axis 0: ", j.get_axis(0), "Axis 1:", j.get_axis(1), "Axis 2:", j.get_axis(2), "Axis 3:", j.get_axis(3)#, "Axis 11:", j.get_axis(11)
            print "B0:", j.get_button(0), "B1:", j.get_button(1), "B2:", j.get_button(2), "B3:", j.get_button(3), "B4:", j.get_button(4), "B5:", j.get_button(5), "B6:", j.get_button(6), "B7:", j.get_button(7), "B8:", j.get_button(8), "B9:", j.get_button(9), "B10:", j.get_button(10), "B11:", j.get_button(11), "B12:", j.get_button(12), "B13:", j.get_button(13), "B14:", j.get_button(14), "B15:", j.get_button(15), "B16:", j.get_button(16)
            clock.tick(10)

except KeyboardInterrupt:
	j.quit()
	sys.exit()
