#!/usr/bin/env python
# coding: utf8
from controller import PS3
from server import Server

Server().start()
print "Aus Server"
PS3().listen()
print "Aus PS3"
