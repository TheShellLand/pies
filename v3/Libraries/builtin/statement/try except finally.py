

try:
    block-1 ...
except Exception1:
    handler-1 ...
except Exception2:
    handler-2 ...
else:
    else-block
finally:
    final-block


'''
The code in block-1 is executed. If the code raises an exception, the various except blocks are tested: if the
exception is of class Exception1, handler-1 is executed; otherwise if it's of class Exception2, handler-2 is
executed, and so forth. If no exception is raised, the else-block is executed.

No matter what happened previously, the final-block is executed once the code block is complete and any raised
exceptions handled. Even if there's an error in an exception handler or the else-block and a new exception is
raised, the code in the final-block is still run.
'''

