#!/usr/bin/env python
# -*- coding: utf8 -*-


import chardet, json

s = b'\xe2\x98\x83' # ☃

chardet.detect(s)

print(json.dumps(chardet.detect(s), indent=4))
{
    "encoding": "windows-1252",
    "confidence": 0.73
}
