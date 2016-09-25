#!/usr/bin/env python3
import operator

""" Exemple issu du livre 'Développer en Python sur Raspberry Pi'.

Ce fichier liste certaines opérations arithmétiques de base.
"""

def int_fois_deux(x):
    """
    Multiplie la variable x par 2 et retourne le résultat.

    @param: x, la variable à multiplier.
    @return: un entier.
    """
    return int(x * 2)

def int_fois_cinq(x):
    """
    Multiplie la variable x par 5 et retourne le résultat.

    @param: x, la variable à multiplier.
    @return: un entier.
    """
    return int(x * 5)

def int_fois_deux_op(x):
    """
    Multiplie la variable x par 2 et retourne le résultat.

    Utilise le module operator pour effectuer la multiplication.

    @param: x, la variable à multiplier.
    @return: un entier
    """
    return operator.mul(x, 2)
