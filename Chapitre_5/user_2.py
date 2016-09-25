#!/usr/bin/env python3
import os
import sys


def format_commande(utilisateur, choix):
    if choix == 'a':
        return '/usr/sbin/useradd -m {0}'.format(utilisateur)
    elif choix == 's':
        return '/usr/sbin/userdel -r {0}'.format(utilisateur)

uid = os.getuid()

if uid != 0:
    print("Vous devez être administrateur pour lancer ce script!")
    sys.exit(1)

choix = input("Souhaitez-vous ajouter/supprimer un utilisateur ? [a/s] ").strip()

if choix not in ('a', 's'):
    print('Réponse non comprise !')
    sys.exit(1)

utilisateur = input("Tapez l'utilisateur à ajouter: ").strip()
commande = format_commande(utilisateur, choix)
retour = os.system(commande)

if retour != 0:
    print("Probleme d'execution du script!")

sys.exit(retour)
