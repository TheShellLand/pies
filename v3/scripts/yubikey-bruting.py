#!/usr/bin/env python3
# -*- coding: utf8 -*-


import sys
import re
import chardet
import time
import itertools
import platform
from string import digits, ascii_lowercase, ascii_uppercase
from subprocess import Popen, PIPE


YUBIKEY_PERSONALIZE_WIN = 'win/bin/ykpersonalize.exe'
YUBIKEY_PERSONALIZE_LINUX = 'linux/ykpers-1.17.2/ykpersonalize'
YK_PROFILE = '-2'  # choose second profile
YK_KEY = '-c'  # 6 bytes hex 00 11 22 33 44 55
YK_PROMPT = '-y'  # always commit
ARRAY_RANGE = 12

if platform.system() == 'Linux':
    YUBIKEY_PERSONALIZE = YUBIKEY_PERSONALIZE_LINUX
else:
    YUBIKEY_PERSONALIZE = YUBIKEY_PERSONALIZE_WIN


YK_KEY_INPUT = input('Input known characters, if any: ')
ARRAY_RANGE = ARRAY_RANGE - len(str(YK_KEY_INPUT))


TOTAL_KEYS = 10 ** ARRAY_RANGE
TESTED_KEYS = 0

TIME_START = time.time()

# alphanumeric
chars = digits + ascii_uppercase + ascii_lowercase

#for a in itertools.product(range(10), repeat=ARRAY_RANGE):
for comb in itertools.product(chars, repeat=ARRAY_RANGE):

    TOTAL_KEYS -= 1
    TESTED_KEYS += 1

    # numeric
    #YK_KEY_GUESS = YK_KEY + YK_KEY_INPUT + ''.join(map(str, a))[::-1]

    YK_KEY_GUESS = YK_KEY + YK_KEY_INPUT + ''.join(comb)[::-1]


    # call([YUBIKEY_PERSONALIZE, YK_PROFILE, YK_KEY_GUESS, YK_PROMPT, '-z'])

    p = Popen([YUBIKEY_PERSONALIZE, YK_PROFILE, YK_KEY_GUESS, YK_PROMPT, '-z'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode

    err_encoding = chardet.detect(err)
    KEY_FAIL = re.findall('Yubikey core error: write error', err.decode(err_encoding['encoding']))
    YK_EXCEPT_1 = re.findall('Invalid access code string:', err.decode(err_encoding['encoding']))

    if not KEY_FAIL and not YK_EXCEPT_1:
        # print('Key Found! ', YK_KEY_GUESS[2:10], sep='')
        print('\n\tKey Found! ', YK_KEY_GUESS[2:], sep='')
        break

    else:
        #print('incorrect key:', YK_KEY_GUESS[2:], '...', 'keys remaining:', TOTAL_KEYS)
        sys.stdout.write('\rincorrect key: {}  keys remaining: {}  keys failed: {}'.format(YK_KEY_GUESS[2:], TOTAL_KEYS, TESTED_KEYS) )

        if TOTAL_KEYS is 0:
            TIME_END = time.time()
            print('\n')
            print('Out of', TESTED_KEYS, 'keys, none worked')
            print('\n')

            if round((TIME_END - TIME_START) / 60) == 0:
                print('Last run took:', TIME_END - TIME_START, 'seconds')
            elif (TIME_END - TIME_START) / 60 < 60:
                print('Last run took:', (TIME_END - TIME_START) / 60, 'minutes')
            elif (TIME_END - TIME_START) / 60 > 60:
                print('Last run took:', (TIME_END - TIME_START) / 60 / 60, 'hours')

print('End')
