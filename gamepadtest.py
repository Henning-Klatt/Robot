#!/usr/bin/python
import pygame

pygame.init()
print "Joystics: ", pygame.joystick.get_count()
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
print "ID: ", my_joystick.get_id()
print "Name: ", my_joystick.get_name()
print "Buttons: ", my_joystick.get_numbuttons()
print "Axis:    ", my_joystick.get_numaxes()
print "Numhats: ", my_joystick.get_numhats()
print "Numballs ", my_joystick.get_numballs()
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


while 1:
    for event in pygame.event.get():
        print "Axis 0: ", my_joystick.get_axis(0), "Axis 1: ", my_joystick.get_axis(1), "Axis 2: ", my_joystick.get_axis(2), "Axis 3: ", my_joystick.get_axis(3)
        print "B0:", my_joystick.get_button(0), "B1:", my_joystick.get_button(1), "B2:", my_joystick.get_button(2), "B3:", my_joystick.get_button(3), "B4:", my_joystick.get_button(4), "B5:", my_joystick.get_button(5), "B6:", my_joystick.get_button(6), "B7:", my_joystick.get_button(7), "B8:", my_joystick.get_button(8), "B9:", my_joystick.get_button(9), "B10:", my_joystick.get_button(10), "B11:", my_joystick.get_button(11), "B12:", my_joystick.get_button(12), "B13:", my_joystick.get_button(13), "B14:", my_joystick.get_button(14), "B15:", my_joystick.get_button(15), "B16:", my_joystick.get_button(16)
        clock.tick(10)

pygame.quit()
