#!/usr/bin/env python
# -*- coding: utf8 -*-


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 31337))
s.send('python says hello nc')
# 20
s.recv(30)
'nc says hello python\n'
s.close()
