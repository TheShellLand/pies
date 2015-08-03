import subprocess
with open('stdout.txt', 'wb') as out, open('stderr.txt', 'wb') as err:
    subprocess.Popen('ls', stdout=out, stderr=err)

# <subprocess.Popen object at 0xa3519ec>
