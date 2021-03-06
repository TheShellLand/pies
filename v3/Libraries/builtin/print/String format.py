

# refer: http://stackoverflow.com/questions/5082452/python-string-formatting-vs-format

#!/usr/bin/python
sub1 = "python string!"
sub2 = "an arg"

a = "i am a %s" % sub1
b = "i am a {0}".format(sub1)

c = "with %(kwarg)s!" % {'kwarg':sub2}
d = "with {kwarg}!".format(kwarg=sub2)

print a    # "i am a python string!"
print b    # "i am a python string!"
print c    # "with an arg!"
print d    # "with an arg!"






# To answer your first question... .format just seems more sophisticated in many ways. An annoying thing about % is also how it can either take a variable or a tuple. You'd think the following would always work:

# "hi there %s" % name

# yet, if name happens to be (1, 2, 3), it will throw a TypeError. To guarantee that it always prints, you'd need to do

# "hi there %s" % (name,)   # supply the single argument as a single-item tuple

# which is just ugly. .format doesn't have those issues. Also in the second example you gave, the .format example is much cleaner looking.

# Why would you not use it?

#     not knowing about it (me before reading this)
#     having to be compatible with Python 2.5

# To answer your second question, string formatting happens at the same time as any other operation - when the string formatting expression is evaluated. And Python, not being a lazy language, evaluates expressions before calling functions, so in your log.debug example, the expression "some debug info: %s"%some_infowill first evaluate to, e.g. "some debug info: roflcopters are active", then that string will be passed to log.debug().
