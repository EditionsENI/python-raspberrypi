#!/usr/bin/env python3
import sys

for numero, arg in enumerate(sys.argv):
    print('Argument#{0}: {1}'.format(numero, arg))
