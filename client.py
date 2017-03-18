#!/usr/bin/env python

import sys, os, gobject
from Tkinter import *
import pygst
pygst.require("0.10")
import gst

# Goto GUI Class
class Prototype(Frame):
    def __init__(self, parent):
        gobject.threads_init()
        Frame.__init__(self, parent)    

        # Parent Object
        self.parent = parent
        self.parent.title("WebCam")
        self.parent.geometry("640x560+0+0")
        self.parent.resizable(width=FALSE, height=FALSE)

        # Video Box
        self.movie_window = Canvas(self, width=640, height=480, bg="black")
        self.movie_window.pack(side=TOP, expand=YES, fill=BOTH)

        # Buttons Box
        self.ButtonBox = Frame(self, relief=RAISED, borderwidth=1)
        self.ButtonBox.pack(side=BOTTOM, expand=YES, fill=BOTH)

        self.closeButton = Button(self.ButtonBox, text="Close", command=self.quit)
        self.closeButton.pack(side=RIGHT, padx=5, pady=5)

        gotoButton = Button(self.ButtonBox, text="Start", command=self.start_stop)
        gotoButton.pack(side=RIGHT, padx=5, pady=5)

        # Set up the gstreamer pipeline
        self.player = gst.parse_launch ("v4l2src ! video/x-raw-yuv,width=640,height=480 ! ffmpegcolorspace ! xvimagesink")

        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.enable_sync_message_emission()
        bus.connect("message", self.on_message)
        bus.connect("sync-message::element", self.on_sync_message)

    def start_stop(self):
        if self.gotoButton["text"] == "Start":
            self.gotoButton["text"] = "Stop"
            self.player.set_state(gst.STATE_PLAYING)
        else:
            self.player.set_state(gst.STATE_NULL)
            self.gotoButton["text"] = "Start"

    def on_message(self, bus, message):
        t = message.type
        if t == gst.MESSAGE_EOS:
            self.player.set_state(gst.STATE_NULL)
            self.button.set_label("Start")
        elif t == gst.MESSAGE_ERROR:
            err, debug = message.parse_error()
            print "Error: %s" % err, debug
            self.player.set_state(gst.STATE_NULL)
            self.button.set_label("Start")

    def on_sync_message(self, bus, message):
        if message.structure is None:
            return
        message_name = message.structure.get_name()
        if message_name == "prepare-xwindow-id":
            # Assign the viewport
            imagesink = message.src
            imagesink.set_property("force-aspect-ratio", True)
            imagesink.set_xwindow_id(self.movie_window.window.xid)

def main():
    root = Tk()
    app = Prototype(root)
    app.pack(expand=YES, fill=BOTH)
    root.mainloop()  


if __name__ == '__main__':
     main()
