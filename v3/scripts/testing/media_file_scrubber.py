import os
import sys
import re
import base64
import getpass
import Crypto.Hash
from Crypto import Random
from Crypto.Cipher import AES


def walking():
    walk_dir = sys.argv[1]

    print('walk_dir = ' + walk_dir)

    # If your current working directory may change during script execution, it's recommended to
    # immediately convert program arguments to an absolute path. Then the variable root below will
    # be an absolute path as well. Example:
    # walk_dir = os.path.abspath(walk_dir)
    print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

    for root, subdirs, files in os.walk(walk_dir):
        print('--\nroot = ' + root)
        list_file_path = os.path.join(root, 'my-directory-list.txt')
        print('list_file_path = ' + list_file_path)

        with open(list_file_path, 'wb') as list_file:
            for subdir in subdirs:
                print('\t- subdirectory ' + subdir)

            for filename in files:
                file_path = os.path.join(root, filename)

                print('\t- file %s (full path: %s)' % (filename, file_path))

                with open(file_path, 'rb') as f:
                    f_content = f.read()
                    list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
                    list_file.write(f_content)
                    list_file.write(b'\n')



# strings
U2FsdGVkX1+h2WCo6BySA6lOFkyYeOp6zndtLw25Z8HjJ/Rk1y5Mc3XT8d5zW9wZ
6utKcxKGUdEYxrfwZPFAtEMgo3pc+vgEh9eETb53TETikm/9ZJmYkMn8Ra+ttiHI
xDEY+NLB/nzrWgc3XhrmOYh8EXTtFq8xAqVPghFvFMigCfYlkNlZ4PszbDXQ3Rgi
lEjRRPEP2KuUWgZ8bVQjI4GrFrtUfPIAdNvsZCrZuxL5cTmn4+Ye2JIAnpT7h8gM
BDhzFU38qQs10m05rbtD0/xfbXnnKlAKOOPVDjx9SumWobqrPjCNwXsBy4dL3jFt
yxBMw2zE0CM6QtMSU3QLf2hFVGBLxVqByp7VnT9mQY/knXYruwf0CM+qJTozIQj+
sxq6CwbTkPoHqH4+qIPdpYiOnd2/jDt1Xc7pd5q3Zl1MKhBCZKrAWUm7pZec3hIO
cbo8kluJLWrtkzFR58w1u0PIE1uD0qyEuu3DJHPNmN16ieI++d3+TkcrrWD8STwp
fI+IOAjyILDUeQrN8fVvW2kHhQwonpNUjQm8BEmS+9caiJN77ol1M421mFZVU6l7
cOUO8KSMuxFTuuNN2Sz4GdLmK/1ZxeDSPLOGFfZukgrIcHogDO1c7H9w8yipNrLf
XVyXtJ/itliznhTJActaDfpbM/C07J4yNqkaQ3iCHOBL03yNUAGQDmhn+xC53TtU
eadXpSqX6dN7r9ySdLuXow==

# Clean folder names
def cleaner():
    patterns = {
        ' ': '_',
        ' - ': '_',

    }

    for p in patterns:
        re.sub(p, )


# Really simple encryption
def strings_enc():
    print('Input program string:')
    key = input()
    #progString = getpass.getpass()
    iv = Random.new().read(AES.block_size)
    obj = AES.new(key, AES.MODE_CBC, iv)
    message = "The answer is no"
    ciphertext = obj.encrypt(message)

    obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
    obj2.decrypt(ciphertext)
    # 'The answer is no'

def decrypt(self, enc):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(self.key, AES.MODE_CBC, iv)
    return self._unpad(cipher.decrypt(enc[AES.block_size:])).decode('utf-8')



# main
strings_enc()
