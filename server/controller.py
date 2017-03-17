#!/usr/bin/env python
# coding: utf8
import os, struct, array
from fcntl import ioctl
import threading
from arduino import moveServo, moveMotor
from numpy import interp

class PS3:
    def listen(self):
        print('Available devices:')

        for fn in os.listdir('/dev/input'):
            if fn.startswith('js'):
                print('  /dev/input/%s' % (fn))

        self.axis_states = {}
        self.button_states = {}

        axis_names = {
            0x00 : 'Ly',
            0x01 : 'Lx',
            0x02 : 'Ry',
            0x05 : 'Rx',
            0x2c : 'Lup',
            0x2d : 'Lright',
            0x2e : 'Ldown',
            0x30 : 'L2',
            0x31 : 'R2',
            0x32 : 'L1',
            0x33 : 'R1',
            0x34 : 'Rup',
            0x35 : 'Rright',
            0x36 : 'Rdown',
            0x37 : 'Rleft',
            0x3b : 'unknown',
            0x3c : 'unknown',
            0x3d : 'unknown',
            0x3e : 'unknown',
        }

        button_names = {
            0x120 : 'select',
            0x121 : 'Laxis',
            0x122 : 'Raxis',
            0x123 : 'start',
            0x12a : 'L1',
            0x12b : 'R1',
            0x12c : 'Rup',
            0x12d : 'Rright',
            0x12e : 'Rdown',
            0x12f : 'Rleft',
            0x124 : 'Lup',
            0x125 : 'Lright',
            0x126 : 'Ldown',
            0x127 : 'Lleft',
            0x128 : 'L2',
            0x129 : 'R2',
            0x2c0 : 'ps',
        }

        self.axis_map = []
        self.button_map = []

        fn = '/dev/input/js0'
        print('Opening %s...' % fn)
        self.jsdev = open(fn, 'rb')

        # Get the device name.
        #buf = bytearray(63)
        buf = array.array('c', ['\0'] * 64)
        ioctl(self.jsdev, 0x80006a13 + (0x10000 * len(buf)), buf) # JSIOCGNAME(len)
        js_name = buf.tostring()
        print('Device name: %s' % js_name)

        # Get number of axes and buttons.
        buf = array.array('B', [0])
        ioctl(self.jsdev, 0x80016a11, buf) # JSIOCGAXES
        num_axes = buf[0]

        buf = array.array('B', [0])
        ioctl(self.jsdev, 0x80016a12, buf) # JSIOCGBUTTONS
        num_buttons = buf[0]

        # Get the axis map.
        buf = array.array('B', [0] * 0x40)
        ioctl(self.jsdev, 0x80406a32, buf) # JSIOCGAXMAP

        for axis in buf[:num_axes]:
            axis_name = axis_names.get(axis, 'unknown(0x%02x)' % axis)
            self.axis_map.append(axis_name)
            self.axis_states[axis_name] = 0.0

        # Get the button map.
        buf = array.array('H', [0] * 200)
        ioctl(self.jsdev, 0x80406a34, buf) # JSIOCGBTNMAP

        for btn in buf[:num_buttons]:
            btn_name = button_names.get(btn, 'unknown(0x%03x)' % btn)
            self.button_map.append(btn_name)
            self.button_states[btn_name] = 0

        print "Axis:   ", num_axes
        print "Buttons:", num_buttons

        self.y = 90
        self.x = 90
        listener = threading.Thread(target=self.get(), args = ())
        listener.start()

    # Main event loop
    def get(self):
        while True:
            evbuf = self.jsdev.read(8)
            if evbuf:
                time, value, type, number = struct.unpack('IhBB', evbuf)

                if type & 0x80:
                     print ("(initial)")

                if type & 0x01:
                    button = self.button_map[number]
                    if button:
                        self.button_states[button] = value
                        if value:
                            if(button == "Lright"):
                                moveServo(0, 180)
                            if(button == "Lleft"):
                                moveServo(0, 700)
                            if(button == "Lup"):
                                moveServo(1, 193)
                            if(button == "Ldown"):
                                moveServo(1, 570)
                            print ("%s pressed" % (button))
                        else:
                            print ("%s released" % (button))
                            if(button == "Lright" or button == "Lleft"):
                                moveServo(0, 380)
                            if(button == "Lup" or button == "Ldown"):
                                moveServo(1, 380)


                if type & 0x02:
                    axis = self.axis_map[number]
                    if axis:
                        fvalue = value / 32767.0
                        self.axis_states[axis] = fvalue
                        #links - rechts
                        if(axis == "Ry"):
                            servovalue = int(round(interp(fvalue, [-1,1], [700,180]), 1))
                            moveServo(0, servovalue)
                        #hoch - runter
                        if(axis == "Rx"):
                            servovalue = int(round(interp(fvalue, [-1,1], [193,570]), 1))
                            moveServo(1, servovalue)
                        if(axis == "Lx"):
                            if(fvalue > 0):
                                motorvalue = int(round(interp(fvalue, [0,1], [0,1000]), 1))
                                moveMotor(3, 0)
                                moveMotor(2, motorvalue)
                            if(fvalue < 0):
                                motorvalue = int(round(interp(fvalue, [-1,0], [0,1000]), 1))
                                moveMotor(2, 0)
                                moveMotor(3, motorvalue)
                        if(axis != "unknown"):
                            print ("%s: %.3f" % (axis, fvalue))
PS3().listen()
