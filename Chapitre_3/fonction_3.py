#!/usr/bin/env python3

def args_nommes(arg1='', arg2=0, arg3=None):
    print('Argument arg1: \'{0}\''.format(arg1))
    print('Argument arg2: {0}'.format(arg2))
    print('Argument arg3: {0}'.format(arg3))

args_nommes()
args_nommes('', 2, 3)
args_nommes(arg3=0, arg1='hi!', arg2=150)
