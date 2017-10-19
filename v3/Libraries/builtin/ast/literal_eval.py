#!/bin/env python3


def literal(obj):
    """ Turn string into tuple
    """

    from ast import literal_eval as make_tuple

    if not obj:
        obj = '(1,2,3,4,5)'

    magic = make_tuple(obj)  # (1, 2, 3, 4, 5)

    return magic

# wow
