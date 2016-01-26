#!/usr/bin/env python

import argparse
import logging

parser = argparse.ArgumentParser(
        description='A test script for http://stackoverflow.com/q/14097061/78845'
)
parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

args = parser.parse_args()
if args.verbose:
    logging.basicConfig(level=logging.DEBUG)

logging.debug('Only shown in debug mode')
