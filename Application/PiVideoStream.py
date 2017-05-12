#!/usr/bin/python3

import socket
import struct
import pickle
import time
from PIL import Image, ImageTk

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    from Tkinter import messagebox

class PiVideoStream(object):
    def __init__(self, gui, host='127.0.0.1', port=8000):
        self.gui = gui
        self.host = host
        self.port = port
        self.running = False

    def start(self, host='127.0.0.1'):
        self.client_socket = socket.socket()
        self.client_socket.settimeout(2)
        try:
            self.client_socket.connect((host, self.port))
        except (socket.timeout, ConnectionRefusedError) as Error:
            print(Error)
            self.gui.streamDummy.place(x=360, y=180)
            tk.messagebox.showerror("Connection Error", str(host) + ": " + str(Error))
            self.stop()
            return
        self.client_socket.settimeout(None)
        # makefile Object aus der Verbindung
        self.connection = self.client_socket.makefile('rb')
        self.running = True

        #self.t = Thread(target=self.update, args=())
        #self.t.setDaemon(1)
        #self.t.start()
        self.update()

        time.sleep(0.2)

    def update(self):
        data_len = struct.unpack('<L', self.connection.read(struct.calcsize('<L')))[0]
        if data_len:
            printD('Updating...')
            printD('data_len: %s' % data_len)
            data = self.connection.read(data_len)
            deserialized_data = pickle.loads(data)
            printD('Frame received')
                #print(deserialized_data)
            img = Image.fromarray(deserialized_data)
            img = img.resize((640,480), Image.ANTIALIAS)
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
        # Länge des Bildes als ein 32-bit Int
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
        self.gui.startstop_button.config(bg="green", text="Start")
        self.gui.ip.config(state="normal")
        self.running = False
        try: self.connection.close()
        except: pass
        try: self.client_socket.close()
        except: pass
        self.client_socket = None
