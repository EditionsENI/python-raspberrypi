#!/usr/bin/env python3
from urllib.request import urlopen
from html.parser import HTMLParser
import threading
import re
import os

url = 'https://fr.wikipedia.org/wiki/France'
imagesdir = './images'


class ParseurHTML(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            tagattrs = dict((x, y) for x, y in attrs)
            img = tagattrs['src']
            if re.search(r'upload', img):
                self.images.append(('https:' + img, os.path.basename(img)))


def sauvegarde_image(obj):
    wwwimage, image = obj
    with urlopen(wwwimage) as entree:
        with open('images/' + image, 'wb') as sortie:
            print('Sauvegarde de {0} ...'.format(image))
            sortie.write(entree.read())


def main():
    if not os.path.exists(imagesdir):
        os.mkdir(imagesdir)

    parseur = ParseurHTML()
    reponse = urlopen(url)
    data = reponse.read().decode('UTF-8')
    parseur.feed(data)

    for obj in parseur.images:
        thread = threading.Thread(target=lambda: sauvegarde_image(obj))
        thread.start()

if __name__ == '__main__':
    main()
