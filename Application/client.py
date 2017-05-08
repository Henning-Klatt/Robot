import socket
import pygame
import sys

host = "192.168.1.1"
port=5000
screen = pygame.display.set_mode((1280,720),0)
pygame.display.set_caption("LexoBot Remote")

while True:
    clientsocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((host, port))
    received = []
    while True:
        recvd_data = clientsocket.recv(230400)
        if not recvd_data:
            break
        else:
            received.append(recvd_data)

    dataset = b''.join(v for v in received)
    image = pygame.image.fromstring(dataset,(320,240),"HSV")
    image = pygame.transform.scale(image, (640, 480))
    screen.blit(image,(0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.display.toggle_fullscreen()
                print("Toggle Fullscreen")
