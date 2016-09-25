#!/usr/bin/env python3

class Voiture:
    def __init__(self, annee=0):
        self.annee = annee

    def __str__(self):
        return 'Je suis une voiture de l\'année {annee}.'.format(
            annee=self.annee
        )

class Peugeot(Voiture):
    def __init__(self, annee, slogan):
        super().__init__(annee)
        self.slogan = slogan

    def __str__(self):
        return super().__str__() + \
            ' Je suis de marque Peugeot.' + \
            ' Mon slogan: {slogan}'.format(
            slogan=self.slogan
        )

v1 = Voiture(annee=2000)
print(v1)
v2 = Peugeot(annee=2002, slogan='Passion for life.')
print(v2)
