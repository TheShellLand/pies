import os
import glob

for f in glob.glob('*.py'):
    if os.stat(f).st_size > 6000