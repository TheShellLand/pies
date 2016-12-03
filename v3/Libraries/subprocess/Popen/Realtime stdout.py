import subprocess

myproc = subprocess.Popen('<cmd> 1>&2', stderr=subprocess.PIPE)