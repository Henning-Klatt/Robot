import pygame

pygame.init()
print "Joystics: ", pygame.joystick.get_count()
my_joystick = pygame.joystick.Joystick(0)
my_joystick.init()
clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        print "0:" + my_joystick.get_axis(0),  "1: " + my_joystick.get_axis(1), "2: " + my_joystick.get_axis(2), "3: " + my_joystick.get_axis(3) 
        clock.tick(40)

pygame.quit()
