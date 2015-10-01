#!/usr/bin/env python
# -*- coding: utf8 -*-




'''
You can remove all non-word characters in the following way:

#>>> re.sub(r'[^\w]', '', 'MagX\x00\x00\x00\x08\x01\x008\xe6\x7f')
'MagX8'

The regex [^\w] will match any character that is not a letter, digit, or underscore. By providing that regex in re.sub with an empty string as a replacement you will delete all other characters in the string.

Since there may be other characters you want to keep, a better solution might be to specify a larger range of characters that you want to keep that excludes control characters. For example:

#>>> re.sub(r'[^\x20-\x7e]', '', 'MagX\x00\x00\x00\x08\x01\x008\xe6\x7f')
'MagX8'

Or you could replace [^\x20-\x7e] with the equivalent [^ -~], depending on which seems more clear to you.

To exclude all characters after this first control character just add a .*, like this:

#>>> re.sub(r'[^ -~].*', '', 'MagX\x00\x00\x00\x08\x01\x008\xe6\x7f')
'MagX'

'''

import re
import sys
import os


def hex_cleanup(*args):
    if len(sys.argv) == 1:
        print('No arguments, exiting')
        return None
    else:
        print('[*] Input file: ' + sys.argv[1])
        f, ext = os.path.splitext(sys.argv[1])
        print('[*] Output file: ' + f + '-cleaned' + ext + '\n\n')
        f = open(f + '-cleaned' + ext, 'w')
        with open(sys.argv[1], 'r') as source_file:
            for line in source_file:
                print('Line: ' + line)
                cleaned = re.sub(r'\xa0', ' ', line)
                print('Cleaned: ' + cleaned)
                f.write(cleaned)
        print('[*] Done')




if __name__ == "__main__":
    hex_cleanup()