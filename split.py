#!/usr/bin/env python3


"""renote: re split module
"""


import re


def my_split(word):
    """renote: re split function
    """

    pattern = re.compile(r' +')
    res = pattern.split(word)

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
            my_split(enter_word)

        print('>>> ', end='')
