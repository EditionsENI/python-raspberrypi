#!/usr/bin/env python3

class Voiture:
    def __init__(self, marque='', annee=0):
        self.marque = marque
        self.annee = annee
        print(self)

    def __str__(self):
        return "Je suis une voiture:\n{marque}\n{annee}".format(
            marque=self.marque,
            annee=self.annee
        )

class Marque:
    def __init__(self, nom=''):
        self.nom = nom

    def __str__(self):
        if self.nom == 'Peugeot':
            slogan = 'La marque au lion'
        elif self.nom == 'Renault':
            slogan = 'Passion for life'
        else:
            slogan = 'Aucun'
        return '{marque}: {slogan}'.format(
            marque=self.nom,
            slogan=slogan
        )

class Annee:
    def __init__(self, annee=0):
        self.annee = annee

    def __str__(self):
        return 'Annee: {annee}'.format(
            annee=self.annee
        )

v1 = Voiture(marque=Marque('Peugeot'), annee=Annee(1999))
v2 = Voiture(marque=Marque('Renault'), annee=Annee(2009))
