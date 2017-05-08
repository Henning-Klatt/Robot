import socket
import pygame
import pygame.camera
import sys
import time

port = 5000
pygame.init()

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(("",port))
serversocket.listen(1)

pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0",(320,240))
cam.set_controls(hflip = True, vflip = False)
cam.start()

while True:
        connection, address = serversocket.accept()
        image = cam.get_image() # capture image
        data = pygame.image.tostring(image,"RGB") # convert captured image to string, use RGB color scheme
        connection.sendall(data)
        time.sleep(0.005)
        connection.close()
