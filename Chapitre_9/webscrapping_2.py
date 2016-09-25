#!/usr/bin/env python3
from urllib.request import urlopen
from html.parser import HTMLParser
import re

url = 'https://fr.wikipedia.org/wiki/France'


class ParseurWiki(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            tagattrs = dict((x, y) for x, y in attrs)
            img = tagattrs['src']
            if re.search(r'upload', img):
                print('https:' + img)


def main():
    reponse = urlopen(url)
    data = reponse.read().decode('UTF-8')
    ParseurWiki().feed(data)

if __name__ == '__main__':
    main()
