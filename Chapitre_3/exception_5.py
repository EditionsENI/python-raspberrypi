#!/usr/bin/env python3
class CrashException(BaseException):
    pass

try:
    print('Je veux voler!')
    raise CrashException('Mayday!')
except CrashException as crash:
    print(".. mais l'Homme ne vole pas.")
    print('Attention! {0}'.format(crash))
finally:
    print('Atterissage...')
