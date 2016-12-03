
# stdin, stdout and stderr specify the executed programs’ standard input, standard output and standard error
# file handles, respectively. Valid values are PIPE, an existing file descriptor (a positive integer), an
# existing file object, and None.

## Some rules of thumb for subprocess
# Never use shell=True. It needlessy invokes an extra shell process to call your program.
# When calling processes, arguments are passed around as lists. sys.argv in python is a list, and so is argv in C. So you pass a list to Popen to call subprocesses, not a string.
# Don't redirect stderr to a PIPE when you're not reading it.
# Don't redirect stdin when you're not writing to it.
