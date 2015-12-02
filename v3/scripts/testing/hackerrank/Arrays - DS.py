import re


LEN = int(input().strip())
ARRAY = input().strip()


ARRAY_list = ARRAY.split(' ')
index = LEN


#print('Length of array:', LEN)


if LEN == len(re.findall('[0-9]+', ARRAY)):
    print(' '.join(ARRAY_list[::-1]))
else:
    print('Length not equal to array. Exiting')
    exit(1)

