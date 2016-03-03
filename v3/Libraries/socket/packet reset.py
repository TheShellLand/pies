#!/usr/bin/env python
# -*- coding: utf8 -*-

import socket


# Send TCP reset packet
def client(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    s.connect((host, port))
    l_onoff = 1
    l_linger = 0
    s.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER,
                 struct.pack('ii', l_onoff, l_linger))
    # send data here
    s.close()
