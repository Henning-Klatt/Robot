import socket

import pygame

import sys



port=5000



#create pygame screen

screen = pygame.display.set_mode((800,600),0)



while True:

    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.bind(("",port)) # server is available on the whole network by setting host to ""

    s.listen(1)

    connection, addr = s.accept()

    received = []



    # loop .recv, it returns empty string when done, then transmitted data is completely received

    while True:

        recvd_data = connection.recv(1440021)

        if not recvd_data:

            break

        else:

            received.append(recvd_data)



    dataset = ''.join(received)

    image = pygame.image.fromstring(dataset,(800,600),"RGB") # convert received image from string

    #image = pygame.transform.scale(image,(800,600)) # scale image to 800*600

    screen.blit(image,(0,0)) # "show image" on the screen

    pygame.display.update()



    # check for quit events

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            sys.exit()
