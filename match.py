#!/usr/bin/env python3


"""renote: re match module
"""


import re


def my_match(word):
    """renote: re match function
    """

    pattern = re.compile(r'Python3')
    res = pattern.match(word)

    if res:
        print('OK')
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
            my_match(enter_word)

        print('>>> ', end='')
