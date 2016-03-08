#!/usr/bin/env python
# -*- coding: utf8 -*-

import string
import binascii
import chardet


def strings_file(filename, min=4):
    with open(filename, "rb") as f:
        result = ""
        for c in f.read():
            if c in string.printable:
                result += c
                continue
            if len(result) >= min:
                yield result
            result = ""


def strings(blob, min=4):
    result = ""
    for c in blob:
        if c in string.printable:
            result += c
            continue
        if len(result) >= min:
            yield result
        result = ""


file = r'Thumbs.db'
OUT = open(file, 'rb')

list_of_encodings = []

with open(file, 'rb') as read_file:
    for line in read_file:

        try:

            add_to_list = chardet.detect(line)['encoding']

            if add_to_list not in list_of_encodings:
                list_of_encodings.append(add_to_list)

        except:
            None

print(list_of_encodings)

for encoding in list_of_encodings:

    try:
        if encoding:
            with open(file, 'rb') as read_file:
                print('---\nEncoding:', encoding, '\nDecoded:', read_file.read().decode(encoding=encoding))

    except UnicodeDecodeError:
        None



with OUT as read_file:
    for LEN in range(4, 15):
        for i in strings(OUT, LEN):
            print('MINLENGTH>', LEN, '    ', i)