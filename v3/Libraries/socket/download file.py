#!/usr/bin/env python
# -*- coding: utf8 -*-


import os
import sys
import urllib3
import shutil


def usage():
    print('Usage:', os.path.basename(__file__), '[URL]', '[SAVE LOCATION]')
    print()


def main(download_file, location):

    chunk_size = 4096
    path, name = os.path.split(download_file)
    saved_file = location + '\\' + name
    temp_save_file = saved_file + '.incomplete'

    print('Download URL:', download_file)
    print('File name:', name)
    print('Save Location:', saved_file)

    http = urllib3.PoolManager()
    response = http.request('GET', download_file)

    with open(temp_save_file, 'wb') as f:

        while True:
            data = response.read(chunk_size)
            if data is None:
                break
            else:
                f.write(data)
                print('Written:', len(data))
        f.close()

        if os.path.isfile(temp_save_file):
            shutil.move(temp_save_file, saved_file)
            print('Download complete')
        else:
            print('Error saving file!')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()

        download_file = input('Download URL: ')
        location = input('Save Location: ')

        main(download_file, location)

    else:
        main(sys.argv[0], sys.argv[1])
