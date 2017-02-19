#!/usr/bin/env python
# coding: utf8

import gevent

def server():
    print "In Server"
    import server
    print "Aus Server"


def controller():
    print "In Controller"
    import controller
    print "Aus Controller"

gevent.joinall([
    gevent.spawn(server),
    gevent.spawn(controller),
])
