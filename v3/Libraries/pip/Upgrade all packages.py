#!/usr/bin/python3
# -*- coding: utf8 -*-

import pip
import subprocess

try:
    for distribution in pip.get_installed_distributions():
        subprocess.call('python -m pip install --upgrade ' + distribution.project_name, shell=True)
except OSError:
    print('Permission denied')
