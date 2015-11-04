from os.path import basename
import os

# now you can call it directly with basename
print(basename("/a/b/c.txt"))
print(os.path.basename(__file__))