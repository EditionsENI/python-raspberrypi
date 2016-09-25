#!/usr/bin/env python3
ma_liste = [1, 2, 3, 4, 5]
print('Ma liste: {0}'.format(ma_liste))
mon_iter = ma_liste.__iter__()
print('Mon iterateur: {0}'.format(mon_iter))
print('Éléments:')
print(next(mon_iter))
print(next(mon_iter))
print(next(mon_iter))
print(next(mon_iter))
print(next(mon_iter))
print(next(mon_iter))
