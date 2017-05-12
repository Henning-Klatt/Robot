#!/usr/bin/python3

import socket
import struct
import pickle
import picamera
from sys import stdout
from time import sleep, strftime
from picamera.array import PiRGBArray
from threading import Thread


DEBUG=False


def printD(message):
    if DEBUG:
        print('[{}]  {}'.format(strftime('%H:%M:%S'), message))
        stdout.flush()


class PiVideoStream(object):
    def __init__(self, resolution=(320, 240), format='rgb', framerate=24, led=True):
        self.camera_led = led
        self.camera = picamera.PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate
        self.rawCapture = PiRGBArray(self.camera, size=resolution)
        self.stream = self.camera.capture_continuous(self.rawCapture, format=format, use_video_port=True)
        self.frame = None
        self.running = False
        self.start()
        self.stop()

    def start(self):
        printD("videostream: start")
        #Thread um die Frames der Kamera zu lesen
        if self.camera_led:
            self.camera.led = self.camera_led
        self.running = True
        Thread(target=self.update, args=()).start()
        sleep(0.2) #Bisschen Zeit zum starten geben

    def stop(self):
        printD("videostream: stop")
        self.camera.led = False
        self.running = False

    def update(self):
        # Lasse laufen bis Thread gestoppt wird
        for frameBuf in self.stream:
            # Bekomme Frame vom Stream und leere den stream für nächsten frame
            self.frame = frameBuf.array
            self.rawCapture.truncate(0)
            # Stoppe Thread
            if self.running == False:
                return

    def read(self):
        # Gebe Frame zurück
        return self.frame

    def quit(self):
        # Schieße Kamera
        try:
            self.running = False
            self.stream.close()
            self.rawCapture.close()
            self.camera.close()
        except:
            pass



class StreamServer(object):
    def __init__(self, videostream=None, host='0.0.0.0', port=8000):
        self.videostream = videostream
        self.host = host
        self.port = port
        self.running = False
        self.start_socket()

    def start_socket(self):
        self.server_socket = socket.socket()
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        #self.server_socket.setblocking(1)

    def start(self):
        printD("streamserver: start")
        self.running = True
        while self.running:
            frame = self.videostream.read()
            serialized_frame = pickle.dumps(frame)
            data_len = len(serialized_frame)
            printD("data_len: %d" % data_len)
            self.connection.write(struct.pack('<L', data_len))
            self.connection.flush()
            self.connection.write(serialized_frame)
            self.connection.flush()
            printD("send.")
            sleep(0.01)

    def stop(self):
        printD("streamserver: start")
        self.running = False

    def quit(self):
        try:
            self.running = False
            self.videostream.quit()
            try: self.client.close()
            except: pass
            try: self.server_socket.close()
            except: pass
            self.client = None
            self.server_socket = None
        except:
            pass

    def run(self):
        while True:
            print("Waiting for Connection...")
            self.client, self.client_addr = self.server_socket.accept()
            if self.client:
                self.connection = self.client.makefile('wb')
            print("Connected: %s" % self.client_addr[0])
            try:
                self.videostream.start()
                self.start()
            except: pass
            finally:
                print("Disconnected")
                self.stop()
                try: self.videostream.stop()
                except: pass
                try: self.client.close()
                except: pass
                try: self.connection.close()
                except: pass


if __name__ == '__main__':
    stream_resolution = (320, 240)
    stream_framerate = 15
    picamera_led = True

    try:
        vs = PiVideoStream(resolution=stream_resolution, framerate=stream_framerate, led=picamera_led)
        stream = StreamServer(videostream=vs).run()
    except (KeyboardInterrupt, SystemExit):
        try: stream.quit()
        except: pass
        print('\nQuit\n')


#EOF
