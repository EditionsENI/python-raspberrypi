#!/usr/bin/env python3
from xml.etree import ElementTree

def main():
    chemin = 'bdd/commandes.xml'
    with open(chemin, 'r', encoding='UTF-8') as f:
        arbre = ElementTree.parse(f)
        racine = arbre.getroot()
    commandes = racine.find('commandes')
    commande = racine.find("commandes/commande[@code='RP04']")
    print('Suppression de la commande: %s' % (ElementTree.tostring(commande).decode('UTF-8')))
    commandes.remove(commande)
    arbre.write(chemin, encoding='UTF-8', xml_declaration=True)
    print('OK!')

if __name__ == '__main__':
    main()
