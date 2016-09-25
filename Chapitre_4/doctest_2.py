#!/usr/bin/env python3

""" Exemple issu du livre 'Développer en Python sur Raspberry Pi'.

Ce fichier liste certaines opérations arithmétiques de base.
Les fonctions sont testées à l'aide du module 'doctest'.
"""

def int_fois_deux(x):
    """
    Multiplie le paramètre x par 2 et retourne le résultat.

    @param: x, la valeur à multiplier.
    @return: un entier.

    >>> int_fois_deux(2)
    4
    >>> int_fois_deux(8)
    16
    """
    return int(x * 2)


def int_fois_cinq(x):
    """
    Multiplie le paramètre x par 5 et retourne le résultat.

    @param: x, la valeur à multiplier.
    @return: un entier.

    >>> int_fois_cinq(5)
    25
    >>> int_fois_cinq(10)
    50
    >>> int_fois_cinq('a')
    Traceback (most recent call last):
    ValueError: invalid literal for int() with base 10: 'aaaaa'
    """
    return int(x * 5)
