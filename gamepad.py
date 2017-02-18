#!/usr/bin/python
import urllib2
import sys
import pygame

ip = sys.argv[1]
print "IP: " + ip

pygame.init()
print "Joystics: ", pygame.joystick.get_count()
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
print "ID: ", my_joystick.get_id()
print "Name: ", my_joystick.get_name()
print "Buttons: ", my_joystick.get_numbuttons()
print "Numhats: ", my_joystick.get_numhats()
print "Numballs ", my_joystick.get_numballs()
clock = pygame.time.Clock()

select = 0
laxis = 1
raxis = 2
raxis_pressed = False
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
        if(my_joystick.get_button(2)):
            if(raxis_pressed == False):
                #output = urllib2.urlopen("http://" + ip + ":8081/cameramove/?x=80&y=103").read()
                raxis_pressed = True
        else:
            raxis_pressed = False
        x = my_joystick.get_axis(3)
        y = my_joystick.get_axis(2)
        if((x > 0.0 or x < 0.0) and (y > 0.0 or y < 0.0)):
            x = int(round(90-(x / -1.0*90), 1))
            y = int(round(90+(y / -1.0*90), 1))
        if('lastX' in locals() and 'lastY' in locals()):
            if (x != lastX and y != lastY):
                #output = urllib2.urlopen("http://" + ip + ":8081/cameramove/?x=" + str(y) + "&y=" + str(x)).read()
                print "X: " + str(x),  "Y: " + str(y)
        lastX = x
        lastY = y
        clock.tick(40)

pygame.quit()
