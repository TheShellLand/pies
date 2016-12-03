#!/usr/bin/env python
# -*- coding: utf8 -*-

# Python script that checks the running platform

import platform


def main():
    if platform.system() == 'Linux':
        print('Platform is', platform.system())
    elif platform.system() == 'Windows':
        print('Platform is', platform.system())


if __name__ == "__main__":
    main()
