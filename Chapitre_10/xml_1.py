#!/usr/bin/env python3
from xml.etree import ElementTree

def main():
    chemin = 'bdd/commandes.xml'
    print("Génération de '%s' ..." % (chemin))
    xml = ElementTree.XML("""
<body>
    <commandes>
        <commande code="HP03" quantite="2">
            Imprimante HP
        </commande>
        <commande code="RP04" quantite="4">
            Raspberry Pi 1 version B+
        </commande>
        <commande code="IB02" quantite="2">
            Souris IBM
        </commande>
    </commandes>
</body>
""")
    arbre = ElementTree.ElementTree(xml)
    arbre.write(chemin, encoding='UTF-8', xml_declaration=True)
    print('OK!')

if __name__ == '__main__':
    main()
