#!/usr/bin/env python3

mon_tuple = tuple(i for i in range(1, 11) if i % 2 == 0)
print('Avec un tuple: {0}'.format(mon_tuple))
mon_tuple = list(i for i in range(1, 11) if i % 2 == 0)
print('Avec une liste: {0}'.format(mon_tuple))
mon_dict = {x: x**x for x in range(0, 5)}
print('Avec un dictionnaire: {0}'.format(mon_dict))
mon_set = set(i for i in range(1, 11) if i % 2 == 0)
print('Avec un set: {0}'.format(mon_set))
