
int.from_bytes(b'y\xcc\xa6\xbb', byteorder='big') # Default byte ordering
# 2043455163


int.from_bytes(b'y\xcc\xa6\xbb', byteorder='little')
# 3148270713