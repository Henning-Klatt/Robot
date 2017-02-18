#!/usr/bin/env python
# coding: utf8
from controller import PS3
from server import Server

server().start()
PS3().listen()
