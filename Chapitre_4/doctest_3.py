#!/usr/bin/env python3

""" Exemple issu du livre `Développer en Python sur Raspberry Pi'.

La classe 'Opération' liste certaines opérations arithmétiques de base.
Elle est testée à l'aide du module 'doctest'.

"""

class Operations:
    def __init__(self):
        """ Constructeur par défaut. """
        pass

    def int_fois_deux(self, x):
        """
        Multiplie le paramètre x par 2 et retourne le résultat.

        @param: x, la valeur à multiplier.
        @return: un entier.

        >>> op.int_fois_deux(2)
        4
        >>> op.int_fois_deux(8)
        16
        """
        return int(x * 2)

    def int_fois_cinq(self, x):
        """
        Multiplie le paramètre x par 5 et retourne le résultat.

        @param: x, la valeur à multiplier.
        @return: un entier.

        >>> op.int_fois_cinq(5)
        25
        >>> op.int_fois_cinq(10)
        50
        """
        return (x * 5)

if __name__ == '__main__':
    import doctest
    doctest.testmod(extraglobs={'op': Operations()})
