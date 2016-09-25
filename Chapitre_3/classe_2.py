#!/usr/bin/env python3

class Voiture:
    def __init__(self, marque='', annee=0):
        self.marque = marque
        self.annee = annee
        print(self)

    def __str__(self):
        return "Je suis une voiture de marque {marque} annee {annee}".format(
            marque=self.marque,
            annee=self.annee
        )

v1 = Voiture(marque='Renault Clio', annee=2009)
v1 = Voiture(marque='Peugeot 106', annee=1999)
