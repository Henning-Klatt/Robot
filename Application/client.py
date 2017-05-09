#!/usr/bin/python3

import socket
import struct
import pickle
import tkinter as tk
from sys import exit, stdout
import time
from PIL import Image, ImageTk
#from threading import Thread

from multiprocessing import Process

DEBUG=True

def printD(message):
    if DEBUG:
        print('[{}]  {}'.format(time.strftime('%H:%M:%S'), message))
        stdout.flush()


class PiVideoStream(object):
    def __init__(self, gui, host='127.0.0.1', port=8000):
        self.gui = gui
        self.host = host
        self.port = port
        self.running = False

    def start(self):
        self.client_socket = socket.socket()
        self.client_socket.settimeout(10)
        try:
            self.client_socket.connect((self.host, self.port))
        except (socket.timeout, ConnectionRefusedError) as Error:
            print(Error)
            self.stop()
            return
        self.client_socket.settimeout(None)
        # Make a file-like object out of the connection
        self.connection = self.client_socket.makefile('rb')
        self.running = True

        #self.t = Thread(target=self.update, args=())
        #self.t.setDaemon(1)
        #self.t.start()
        self.update()
        #self.gui.master.after(70, self.update_2)

        time.sleep(0.2) #give videostream some time to start befor frames can be read

    def update(self):
        #while self.running:
            # Read the length of the image as a 32-bit unsigned int.
        data_len = struct.unpack('<L', self.connection.read(struct.calcsize('<L')))[0]
        if data_len:
            printD('Updating...')
            printD('data_len: %s' % data_len)
            data = self.connection.read(data_len)
            deserialized_data = pickle.loads(data)
            printD('Frame received')
                #print(deserialized_data)
            img = Image.fromarray(deserialized_data)
            #img = img.resize((800,600), Image.ANTIALIAS)
            newImage = ImageTk.PhotoImage(img)
            self.gui.stream_label.configure(image=newImage)
            self.gui.stream_label.image = newImage
            printD("image updated")
        else:
            time.sleep(0.1)
        if(self.running):
            self.gui.stream_label.after(66, self.update)

    def update_2(self):
        if self.running == False:
            return
        # Read the length of the image as a 32-bit unsigned int.
        data_len = struct.unpack('<L', self.connection.read(struct.calcsize('<L')))[0]
        if data_len:
            printD('Updating...')
            printD('data_len: %s' % data_len)
            data = self.connection.read(data_len)
            deserialized_data = pickle.loads(data)
            printD('Frame received')
            #print(deserialized_data)
            stdout.flush()
            img = Image.fromarray(deserialized_data)
            newImage = ImageTk.PhotoImage(img)
            self.master.stream_label.configure(image=newImage)
            self.master.stream_label.image = newImage
        self.gui.master.after(70, self.update_2)

    def quit(self):
        try: self.stop()
        except: pass

    def stop(self):
        # indicate that the thread should be stopped
        self.running = False
        try: self.connection.close()
        except: pass
        try: self.client_socket.close()
        except: pass
        self.client_socket = None


class GUI(object):
    def __init__(self, resolution="640x480", stream_resolution=(320, 240), host='127.0.0.1', port=8000):
        self.host = host
        self.port = port
        self.gui_resolution = resolution
        self.stream_resolution = stream_resolution
        self.running = False
        self.master = tk.Tk()
        self.master.protocol("WM_DELETE_WINDOW", self.quit)
        self.main()

    def keypress(self, event):
        print("Pressed: " + repr(event.char))

    def keyrelease(self, event):
        print("Released: " + repr(event.char))

    def main(self):
        self.videostream = PiVideoStream(gui=self, host=self.host, port=self.port)
        self.master.geometry(self.gui_resolution)
        self.master.title("LexoBot Remote")
        self.master.bind("<KeyPress>", self.keypress)
        self.master.bind("<KeyRelease>", self.keyrelease)
        self.startstop_button = tk.Button(master=self.master, text="Start", bg="green", command=self.startstop_stream)
        self.startstop_button.place(x=10, y=10, height=50, width=50)
        self.stream_label = tk.Label(master=self.master)
        self.stream_label.place(x=60, y=10)
        self.exit_button = tk.Button(master=self.master, bg="#229", fg="white", text="Exit", command=self.quit)
        self.exit_button.place(x=10, y=200, height=50, width=50)
        self.timeLabel = tk.Label(master=self.master, text="Loading time", fg="black")
        self.timeLabel.place(x=300, y=300)

    def startstop_stream(self):
        # start
        if self.running == False:
            printD("Start")
            self.startstop_button.config(bg="red", text="Stop")
            self.running = True
            self.videostream.start()
        # stop
        else:
            printD("Stop")
            self.startstop_button.config(bg="green", text="Start")
            self.running = False
            self.videostream.stop()

    def run(self):
        self.master.mainloop()

    def quit(self):
        self.running = False
        self.videostream.quit()
        self.master.destroy()
        print('\nQuit\n')


def main(DEBUG=True):
    screen_width  = 400
    screen_height = 300
    stream_resolution = (640, 480)

    try:

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


#EOF
