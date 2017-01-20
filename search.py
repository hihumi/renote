#!/usr/bin/env python3


"""renote: re search module
"""


import re


def my_search(word):
    """renote: re search function
    """

    pattern = re.compile(r'Python3')
    res = pattern.search(word)

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
            my_search(enter_word)

        print('>>> ', end='')
