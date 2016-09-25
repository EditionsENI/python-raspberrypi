#!/usr/bin/env python3

def args_nommes(arg1='', arg2=0, arg3=None):
    print('Argument arg1: \'{0}\''.format(arg1))
    print('Argument arg2: {0}'.format(arg2))
    print('Argument arg3: {0}'.format(arg3))

args = {
    'arg1': 'Bonjour!',
    'arg2': 150,
    'arg3': 3000
}
args_nommes(**args)
