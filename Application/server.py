import socket

import pygame

import pygame.camera

import sys

import time



#host = "192.168.100.9"

host = "192.168.1.64"

port = 5000





pygame.init()

pygame.camera.init()



cam_list = pygame.camera.list_cameras() # list available cameras

webcam = pygame.camera.Camera(cam_list[0],(800,600)) # use first camera in list and set resolution

webcam.start() # start camera



while True:

    image = webcam.get_image() # capture image

    data = pygame.image.tostring(image,"RGB") # convert captured image to string, use RGB color scheme

    #print sys.getsizeof(data) # in case somebody wants to know the size of the captured image



    # prepare for connection to server

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP is used

    s.connect((host, port))

    s.sendall(data)

    s.close()

    time.sleep(0.1)
