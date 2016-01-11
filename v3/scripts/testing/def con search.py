#!/usr/bin/env python
# -*- coding: utf8 -*-


import os
import re
import chardet


os.chdir(r'def con\DEF CON Conference Programs')


search = 'free'


for fileFromList in os.listdir():
    print('Opening:', fileFromList, '... ', end='')
    with open(fileFromList, 'rb') as fileOpenHandle:
        fileDecode = chardet.detect(fileOpenHandle.read(1024))
        fileEncoding = fileDecode['encoding']
        fileSearchCompile = re.compile(search, re.I)
        print('Searching:', search, '... ', end='')
        with open(fileFromList, 'rb') as fileRead:
            #print(fileRead.read(50), '... ', end='')
            if fileSearchCompile.search(str(fileRead.read())):
                print('Search Match in', fileFromList)
            else:
                print('not found')
