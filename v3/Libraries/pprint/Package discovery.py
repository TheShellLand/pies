#!/usr/bin/env python3
# encoding: utf-8

import pip
from pprint import pprint


def print_variables_of(obj):
    """variables of an object"""
    pprint (vars(obj))


def print_callables_of(obj):
    """callables (functions too) of an object"""
    li = []
    for name in dir(obj):
        attr = getattr(obj, name)
        if hasattr(attr, '__call__'):
            li.append(name)
    pprint(li)


def main():
    dist = pip.get_installed_distributions()[0]
    print_variables_of(dist)
    print("-" * 20)
    print_callables_of(dist)

##############################################################################

if __name__ == "__main__":
    main()