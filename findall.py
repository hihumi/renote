#!/usr/bin/env python3


"""renote: re findall module
"""


import re


def my_findall(word):
    """renote: re findall function
    """

    pattern = re.compile(r'Python3Python')
    res = pattern.findall(word)

    if res:
        print('OK')
        print('{}'.format(res))
    else:
        print('NG')

if __name__ == '__main__':
    print('文字列を入力 終了するにはq, Qキー')
    print('>>> ', end='')
    while True:
        enter_word = input()

        if enter_word == 'q' or enter_word == 'Q':
            print('終了')
            break
        elif enter_word:
            my_findall(enter_word)

        print('>>> ', end='')
