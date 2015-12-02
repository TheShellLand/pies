#!/bin/python3

import sys


n = int(input().strip())
level = 1

def treeSpaces(level):
    NumOfSpaces = abs(level - n) # 6 - 1 = 5
    #print('Number of spaces:', NumOfSpaces)
    return ' ' * NumOfSpaces


def treeParts(level):
    NumOfParts = level # 1
    #print('Number of parts:', NumOfParts)
    return '#' * NumOfParts


while level < n + 1:
    # print treeSpaces() + treeParts() for level
    print('{s}{t}'.format(s=treeSpaces(level), t=treeParts(level)))
    level += 1
