#!/usr/bin/env python3


"""renote: template module
"""


import re


def re_template(word):
    """renote: template function
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
            re_template(enter_word)

        print('>>> ', end='')
