#!/bin/python3

import sys


time = input().strip()
twelvehour = time.split(':')
if twelvehour[2][2:] == 'PM':
    twelvehour[2] = twelvehour[2][:2]
    int_list = [int(i) for i in twelvehour]
    if int_list[0] < 12:
        int_list[0] = int_list[0] + 12
    print('%02d:%02d:%02d' % (int_list[0], int_list[1], int_list[2]))
elif twelvehour[2][2:] == 'AM':
    twelvehour[2] = twelvehour[2][:2]
    int_list = [int(i) for i in twelvehour]
    if int_list[0] == 12:
        int_list[0] = 0
    print('%02d:%02d:%02d' % (int_list[0], int_list[1], int_list[2]))