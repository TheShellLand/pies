#!/usr/bin/env python
# -*- coding: utf8 -*-


# http://stackoverflow.com/questions/1728376/get-a-list-of-all-the-encodings-python-can-encode-to

import chardet, json

s = b'\xe2\x98\x83' # ☃

print(chardet.detect(s))

#{'encoding': 'windows-1252', 'confidence': 0.73}