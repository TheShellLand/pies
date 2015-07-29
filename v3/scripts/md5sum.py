import hashlib, sys


def checksum_md5(filename):
    md5 = hashlib.md5()
    with open(filename, 'rb') as f:
        # You can just as effectively use a block size of any multiple of 128 (say 8192, 32768, etc.) and that will be
        # much faster than reading 128 bytes at a time
        for chunk in iter(lambda: f.read(8192), b''):
            # Note that the iter() func needs an empty byte string for the returned iterator to halt at EOF, since
            # read() returns b'' (not just '').
            md5.update(chunk)

    return md5.digest()