#!/usr/bin/env python3
from tkinter import *
import glob, sys, os

class PiVision(Tk):
    def __init__(self, images):
        Tk.__init__(self)
        self.creer_composants()
        if len(images) > 0:
            self.initialiser_images()
            self.afficher_image()
        else:
            self.afficher_erreur()
        self.mainloop()

    def initialiser_images(self):
        liste_image = [(PhotoImage(file=image), os.path.basename(image)) for image in sorted(images)]
        premiere = derniere = VImage(info=liste_image.pop(0))
        for image in liste_image:
            derniere = derniere.ajout(info=image)
        derniere.suivante = premiere
        premiere.precedente = derniere
        self.image_courante = premiere

    def creer_composants(self):
        self.composant_image = Label(self)
        self.composant_image.pack(expand=YES, fill=BOTH)
        self.bouton_frame = Frame(self)
        self.bouton_frame.pack(side=BOTTOM)
        self.bouton_precedent = Button(self.bouton_frame, text='Précédent', command=lambda: self.image_precedente())
        self.bouton_precedent.pack(side=LEFT)
        self.bouton_suivant = Button(self.bouton_frame, text='Suivant', command=lambda: self.image_suivante())
        self.bouton_suivant.pack(side=LEFT)
        self.bouton_fermer = Button(self.bouton_frame, text='Fermer', command=self.destroy)
        self.bouton_fermer.pack(side=LEFT)
        self.bind('<Left>', lambda ev: self.image_precedente())
        self.bind('<Right>', lambda ev: self.image_suivante())
        self.bind('<Escape>', lambda ev: self.destroy())

    def image_suivante(self):
        self.image_courante = self.image_courante.suivante
        self.afficher_image()

    def image_precedente(self):
        self.image_courante = self.image_courante.precedente
        self.afficher_image()

    def afficher_image(self):
        image, nom_image = self.image_courante.info
        self.composant_image.config(image=image)
        self.title('%s - %s ' % (self.__class__.__name__, nom_image))
        self.update()

    def afficher_erreur(self):
        self.bouton_precedent.configure(state='disable')
        self.bouton_suivant.configure(state='disable')
        self.unbind('<Left>')
        self.unbind('<Right>')
        self.erreur = Message(self.composant_image,
                text="Aucune image n'a été trouvée !",
                pady=25, padx=25, aspect=800)
        self.erreur.config(font=('courier', 14, 'bold'))
        self.erreur.pack(expand=YES, fill=BOTH)
        self.title('Erreur!')
        self.update()

class VImage:
    def __init__(self, info, suivante=None, precedente=None):
        self.info = info
        self.suivante = suivante
        self.precedente = precedente

    def ajout(self, info):
        self.suivante = VImage(info, None, self)
        return self.suivante

if __name__ == '__main__':
    def usage(message=''):
        print(message)
        sys.exit(1)

    if len(sys.argv) != 2:
        usage('Veuillez indiquer un répertoire!')

    repertoire = sys.argv[1]
    if not os.path.isdir(repertoire):
        usage("\"{r}\" n'est pas un répertoire!".format(r=repertoire))

    extensions = 'png jpg jpeg gif'.split()
    extensions = extensions + list(map(str.upper, extensions))
    images = []
    for ext in extensions:
        images.append(glob.glob('{}/*.{}'.format(repertoire, ext)))

    images = sum(images, [])
    PiVision(images)
