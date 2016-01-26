#!/usr/bin/env python
# -*- coding: utf8 -*-

#
# Python script to compile and compare locally installed programs with files listed in the repository
# If the file doesn't exist in the repository, delete it, or move it to another folder
#

import os
import platform
import re
import chardet
import argparse
import logging
from subprocess import Popen, PIPE

# Argparse
# add logging todo
parser = argparse.ArgumentParser(description='A script for condensing local repository')
parser.add_argument('-v', '--verbose', help='increase output verbosity', action='store_true')
args = parser.parse_args()

if args.verbose:
    logging.basicConfig(level=logging.DEBUG)

logging.info('Begin script')

# Variables
localPath = '.'


def fileList(localPath):
    # list files todo
    os.chdir(localPath)
    listD = ['ls']
    fList = Popen(listD, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = fList.communicate()

    if args.verbose:
        logging.debug('Start listing files')
        if output:
            print(output.decode(chardet.detect(output)['encoding']))
        if err:
            print('stderr:', err.decode(chardet.detect(err)['encoding']))
        logging.debug('Stop listing files')


def depList():
    # list dependencies todo
    pass


def main():
    if platform.system() == 'Linux':
        pass
    else:
        print('Platform is not Linux. Exiting')
        exit()

    fileList(localPath)
    '''
    fileListRe = r'^\w*'
    reC = re.compile(fileListRe)
    '''

    logging.info('End of program')


if __name__ == "__main__":
    main()
