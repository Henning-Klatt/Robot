#!/usr/bin/python3

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    from Tkinter import messagebox

from sys import exit, stdout
#from threading import Thread

from GUI import GUI
from PiVideoStream import PiVideoStream

DEBUG=False
has_prev_key_release = None

def printD(message):
    if DEBUG:
        print('[{}]  {}'.format(time.strftime('%H:%M:%S'), message))
        stdout.flush()


class inputDevice(object):
    def __init__(self):
        self.gamepad = 0
        #pygame.init()
        #self.t = Thread(target=self.listen, args=())
        #self.t.setDaemon(1)
        #self.t.start()

    def listen(self):
        events = pygame.event.get()
        while True:
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        print("Links")
                    if event.key == pygame.K_RIGHT:
                        print("Rechts")


def main(DEBUG=True):
    screen_width  = 400
    screen_height = 300
    stream_resolution = (320, 240)

    try:

        listener = inputDevice()
        tkinter_app = GUI(host='192.168.1.1', port=8000, resolution="1440x900", stream_resolution=stream_resolution)
        tkinter_app.run()

    except (KeyboardInterrupt, SystemExit):
        print('Quit')
        tkinter_app.quit()
    except Exception as error:
        print('Error: ' + str(error))
        exit()


if __name__ == '__main__':
    main()
