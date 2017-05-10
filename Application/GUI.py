#!/usr/bin/python3

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    import Tkinter as tk
    from Tkinter import messagebox

from PiVideoStream import PiVideoStream

class GUI(object):
    def __init__(self, resolution="640x480", stream_resolution=(320, 240), host='127.0.0.1', port=8000):
        self.host = host
        self.port = port
        self.s1value = 90
        self.s2value = 90
        self.gui_resolution = resolution
        self.stream_resolution = stream_resolution
        self.running = False
        self.master = tk.Tk()
        self.master.protocol("WM_DELETE_WINDOW", self.quit)
        self.main()

    def keypress(self, event):
        print("Pressed: " + event.keysym)
        if(event.keysym == "w"):
            self.m1.set(100)
            self.m2.set(100)
            self.m1Label.config(font="Arial 16 bold")
            self.m2Label.config(font="Arial 16 bold")
        if(event.keysym == "s"):
            self.m1.set(-100)
            self.m2.set(-100)
            self.m1Label.config(font="Arial 16 bold")
            self.m2Label.config(font="Arial 16 bold")
        if(event.keysym == "a"):
            self.m1.set(-100)
            self.m2.set(100)
            self.m1Label.config(font="Arial 16 bold")
            self.m2Label.config(font="Arial 16 bold")
        if(event.keysym == "d"):
            self.m1.set(100)
            self.m2.set(-100)
            self.m1Label.config(font="Arial 16 bold")
            self.m2Label.config(font="Arial 16 bold")

    def keyrelease(self, event):
        global has_prev_key_release
        has_prev_key_release = None
        print("Released: " + event.keysym)
        if(event.keysym == "w" or event.keysym == "s" or event.keysym == "a" or event.keysym == "d"):
            self.m1.set(0)
            self.m2.set(0)
            self.m1Label.config(font="Arial 16")
            self.m2Label.config(font="Arial 16")

    def keyrelease_repeat(self, event):
        global has_prev_key_release
        has_prev_key_release = self.master.after_idle(self.keyrelease, event)

    def keypress_repeat(self, event):
        if(event.keysym == "Left"):
            if(self.s1value > 0):
                self.s1value = self.s1value-10
                self.s1.set(self.s1value)
                print("Servo 1: " + str(self.s1value))
        elif(event.keysym == "Right"):
            if(self.s1value < 180):
                self.s1value = self.s1value+10
                self.s1.set(self.s1value)
                print("Servo 1: " + str(self.s1value))
        elif(event.keysym == "Down"):
            if(self.s2value > 0):
                self.s2value = self.s2value-10
                self.s2.set(self.s2value)
                print("Servo 2: " + str(self.s2value))
        elif(event.keysym == "Up"):
            if(self.s2value < 180):
                self.s2value = self.s2value+10
                self.s2.set(self.s2value)
                print("Servo 2: " + str(self.s2value))
        else:
            global has_prev_key_release
            if has_prev_key_release:
                self.master.after_cancel(has_prev_key_release)
                has_prev_key_release = None
            else:
                self.keypress(event)


    def main(self):
        self.videostream = PiVideoStream(gui=self, host=self.host, port=self.port)
        self.master.geometry(self.gui_resolution)
        self.master.configure(background='#FFFFFF')
        self.master.title("LexoBot Remote")
        self.master.bind("<KeyPress>", self.keypress_repeat)
        self.master.bind("<KeyRelease>", self.keyrelease_repeat)
        self.startstop_button = tk.Button(master=self.master, text="Start",  command=self.startstop_stream)
        self.stream_label = tk.Label(master=self.master)
        self.resolutions = ["320x240", "640x480"]
        self.resolution = tk.StringVar(self.master)
        self.resolution.set('320x240')
        self.resoption = tk.OptionMenu(self.master, self.resolution, *self.resolutions)
        self.ipLabel = tk.Label(self.master, text="IP: ")
        self.ip = tk.Entry(self.master)
        self.ip.insert(10, self.host)
        self.exit_button = tk.Button(master=self.master, text="X", command=self.quit)
        #self.timeLabel = tk.Label(master=self.master, text="Loading time", fg="black")
        self.m1 = tk.Scale(self.master, from_=100, to=-100)
        self.m1.set(0)
        self.m1Label = tk.Label(self.master, text="Motor 1", font="Arial 16")
        self.m2 = tk.Scale(self.master, from_=100, to=-100)
        self.m2.set(0)
        self.m2Label = tk.Label(self.master, text="Motor 2", font="Arial 16")
        self.s1 = tk.Scale(self.master, from_=180, to=0)
        self.s1.set(self.s1value)
        self.s1Label = tk.Label(self.master, text="Servo 1", font="Arial 16")
        self.s2 = tk.Scale(self.master, from_=180, to=0)
        self.s2.set(self.s2value)
        self.s2Label = tk.Label(self.master, text="Servo 2", font="Arial 16")

        #self.timeLabel.place(x=300, y=300)
        self.startstop_button.place(x=600, y=665)
        self.stream_label.place(x=360, y=180)
        self.ipLabel.place(x=360, y=667)
        self.ip.place(x=381, y=665)
        self.exit_button.place(x=1400, y=5)
        self.resoption.place(x=885, y=665)
        self.m1.place(x=360, y=55)
        self.m1Label.place(x=375, y=155)
        self.m2.place(x=420, y=55)
        self.m2Label.place(x=435, y=155)
        self.s1.place(x=480, y=55)
        self.s1Label.place(x=495, y=155)
        self.s2.place(x=540, y=55)
        self.s2Label.place(x=555, y=155)

        if(self.running == False):
            self.streamDummy = tk.Canvas(self.master, width=640, height=480)
            self.streamDummy.create_rectangle(0, 0, 640, 480, fill="black")
            self.streamDummy.place(x=360, y=180)

    def startstop_stream(self):
        # start
        if self.running == False:
            print("Stream Start")
            self.startstop_button.config(bg="red", text="Stop")
            self.ip.config(state="readonly")
            self.streamDummy.place_forget()
            self.host = self.ip.get()
            self.running = True
            self.videostream.start(host=self.host)
        # stop
        else:
            print("Stream Stop")
            self.startstop_button.config(bg="green", text="Start")
            self.ip.config(state="normal")
            self.running = False
            self.videostream.stop()

    def run(self):
        self.master.mainloop()

    def quit(self):
        self.running = False
        self.videostream.quit()
        self.master.destroy()
        print('\nQuit\n')
