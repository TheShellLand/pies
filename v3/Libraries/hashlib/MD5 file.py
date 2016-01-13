import hashlib


print hashlib.md5(open(full_path, 'rb').read()).hexdigest()


[(fname, hashlib.md5(open(fname, 'rb').read()).digest()) for fname in fnamelst]
