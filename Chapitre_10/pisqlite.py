#!/usr/bin/env python3
import sqlite3
import cmd

class PiSQLite(cmd.Cmd):
    def __init__(self, base):
        cmd.Cmd.__init__(self)
        self.prompt = '>> '
        self.intro = 'Bienvenue dans PiSQLite!'
        self.base = base
        self.conn = None

    def connection(self):
        if self.conn == None: self.conn = sqlite3.connect(self.base)
        return self.conn

    def curseur(self):
        return self.connection().cursor()

    def do_creer(self, valeurs):
        """Crée la table 'produits'."""
        try:
            self.curseur().execute('create table produits (code char primary key, nom char, quantite int)')
        except sqlite3.OperationalError:
            print("La table 'produits' existe déjà!")

    def do_inserer(self, valeurs):
        """Insère une entree dans la table 'produits'."""
        valeurs = valeurs.split()
        if len(valeurs) != 3:
            print('Vous devez fournir 3 valeurs!')
            return
        code, nom, quantite = valeurs
        self.curseur().execute(
            'insert into produits values (?, ?, ?)',
            (code, nom, quantite)
        )
        self.connection().commit()

    def do_afficher(self, valeurs):
        """Affiche les entrées présentes dans la table 'produits'."""
        curs = self.curseur().execute('select * from produits')
        resultats = curs.fetchall()
        print('%s resultat(s)' % (len(resultats)))
        for resultat in resultats:
            code, nom, quantite = resultat
            print('=> code: %s, nom: %s, quantité: %s' % (
                code, nom, quantite))

    def do_supprimer(self, valeur):
        """Supprime une entrée dans la table 'produits' en utilisant la clef primaire 'code'."""
        code = valeur.split()
        if len(code) != 1:
            print('Vous devez fournir 1 valeur!')
            return
        self.curseur().execute('delete from produits where code = (?)', code)
        self.connection().commit()

    def do_EOF(self, ligne):
        print("Merci d'avoir utilisé PiSQLite!")
        return -1

    def do_quitter(self, ligne):
        """Ferme le menu."""
        return self.do_EOF(ligne)

if __name__ == '__main__':
    PiSQLite(base='bdd/sqlite3.db').cmdloop()
