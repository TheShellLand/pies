#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys
import os
import hashlib


def chunk_reader(file_object, chunk_size=1024):
    """Generator that reads a file in chunks of bytes"""
    while True:
        chunk = file_object.read(chunk_size)
        if not chunk:
            return
        yield chunk


def check_for_duplicates(paths, hash=hashlib.sha1):
    hashes = {}
    for path in paths:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                hash_object = hash()
                for chunk in chunk_reader(open(full_path, 'rb')):
                    hash_object.update(chunk)
                file_id = (hash_object.digest(), os.path.getsize(full_path))
                duplicate = hashes.get(file_id, None)
                if duplicate:
                    print
                    "Duplicate found: %s and %s" % (full_path, duplicate)
                else:
                    hashes[file_id] = full_path


def main():
    if sys.argv[1:]:
        check_for_duplicates(sys.argv[1:])
    else:
        print
        "Please pass the paths to check as parameters to the script"


if __name__ == "__main__":
    check_for_duplicates(PATH)
