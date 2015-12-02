import re


LEN = int(input().strip())
ARRAY = input().strip()


if LEN == len(re.findall('[0-9]', ARRAY)):
    print(ARRAY[::-1])
else:
    print('Length not equal to array. Exiting')

