#!/usr/bin/env python
# -*- coding: utf8 -*-


import os
import requests


url = 'https://fpdl.vimeocdn.com/vimeo-prod-skyfire-std-us/01/4575/4/122877896/348642579.mp4?token' \
      '=56957066_0x839f46c2194807f9e9fa0b07eaead9df817d2252'

local_dir = '/home/eric/Downloads'


def download_file(url):
    os.chdir(local_dir)
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        chunk_downloaded = 0
        for chunk in r.iter_content(chunk_size=1024):
            print('Downloaded:', round(chunk_downloaded / 1024 / 1024, 2), 'MB')
            if chunk: # filter out keep-alive new chunks
                chunk_downloaded += 1024
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    print('Total size:', chunk_downloaded / 1024, 'KB')
    return local_filename


if __name__ == "__main__":
    download_file(url)
