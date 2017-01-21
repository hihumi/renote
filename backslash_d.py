#!/usr/bin/env python3


"""renote re backslash d
"""


import re
import string


def backslash_d():
    """renote: re backslash d
    """

    printable = string.printable
    print(printable)
    print(repr(printable))
    print()

    pattern1 = re.compile(r'\d')
    res1 = pattern1.findall(printable)
    print('{}'.format(res1))
    print(repr(res1))
    print()

    pattern2 = re.compile(r'\d')
    res2 = pattern2.search(printable)
    print('{}'.format(res2))
    print(repr(res2))
    print()

    pattern3 = re.compile(r'\d')
    res3 = pattern3.match(printable)
    print('{}'.format(res3))
    print(repr(res3))

if __name__ == '__main__':
    backslash_d()
