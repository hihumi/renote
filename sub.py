#!/usr/bin/env python3


"""renote: re sub module
"""


import re


def my_sub(word):
    """renote: re sub function
    """

    pattern = re.compile(r'p')
    res = pattern.sub('P', word)

    if res:
        print('{}'.format(res))
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
            my_sub(enter_word)

        print('>>> ', end='')
