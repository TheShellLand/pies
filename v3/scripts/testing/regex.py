#!/usr/bin/env python
# -*- coding: utf8 -*-
#
import os, re, hashlib
from pprint import pprint


file = input(r'Open file: ')
f = open(file, 'rb')


def hashfile(afile, hasher, blocksize=65536):
    buf = afile.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)

    return hasher.hexdigest()





if __name__ == "__main__":
    hash = hashfile(f, hashlib.sha256())
    print(hash)
