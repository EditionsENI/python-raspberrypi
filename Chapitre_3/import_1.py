#!/usr/bin/env python3
import os

def my_random():
    import random
    print('Voici un nombre généré au hasard:')
    print(random.random())

if os.path.exists('/etc'):
    print('/etc existe!')
    my_random()

print('Le module os? {0}'.format(os))
print('Le module random? {0}'.format(random))
