#!/usr/bin/env python3
from xml.etree import ElementTree

def main():
    with open('bdd/commandes.xml', 'r', encoding='UTF-8') as f:
        xml = ElementTree.parse(f)
        racine = xml.getroot()
    commandes = racine.find('commandes')
    print('Nombre de noeuds dans le noeud \"commandes\": %s' % len(commandes))
    for commande in commandes:
        print('  Nom: %s' % (commande.text.strip()))
        print('  Code: %s' % (commande.attrib['code']))
        print('  Quantite: %s' % (commande.attrib['quantite']))

if __name__ == '__main__':
    main()
