#!/usr/bin/python3
# -*- coding: utf8 -*-

import pip
import subprocess

for distribution in pip.get_installed_distributions():
    subprocess.call('python -m pip install --upgrade ' + distribution.project_name, shell=True)