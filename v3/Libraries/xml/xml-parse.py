#!/usr/bin/env python
# -*- coding: utf8 -*-

import xml.etree.ElementTree as ET
from pprint import pprint

filename = 'GeoLogger.gpx'


def main():
    tree = ET.parse(filename)
    root = tree.getroot()
    pprint(root.tag)
    pprint(root.attrib)
    pprint(root.findtext('.'))


if __name__ == "__main__":
    main()
