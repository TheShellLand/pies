#!/usr/bin/env python
# -*- coding: utf8 -*-




'''
You can remove all non-word characters in the following way:

>>> re.sub(r'[^\w]', '', 'MagX\x00\x00\x00\x08\x01\x008\xe6\x7f')
'MagX8'

The regex [^\w] will match any character that is not a letter, digit, or underscore. By providing that regex in re.sub with an empty string as a replacement you will delete all other characters in the string.

Since there may be other characters you want to keep, a better solution might be to specify a larger range of characters that you want to keep that excludes control characters. For example:

>>> re.sub(r'[^\x20-\x7e]', '', 'MagX\x00\x00\x00\x08\x01\x008\xe6\x7f')
'MagX8'

Or you could replace [^\x20-\x7e] with the equivalent [^ -~], depending on which seems more clear to you.

To exclude all characters after this first control character just add a .*, like this:

>>> re.sub(r'[^ -~].*', '', 'MagX\x00\x00\x00\x08\x01\x008\xe6\x7f')
'MagX'

'''

import re
import sys

def hex_cleanup(*args):
    with open(sys.argv[1], 'r') as my_file:
        print(my_file.read())


filenames = ['file1.txt', 'file2.txt', ...]
with open('path/to/output/file', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)



with open(sys.argv[1], 'r') as my_file:
    print(my_file.read())



if __name__ == "__main__":
    hex_cleanup(*args)