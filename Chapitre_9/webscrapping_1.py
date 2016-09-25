#!/usr/bin/env python3
from urllib.request import urlopen
url = 'https://fr.wikipedia.org/wiki/France'


def main():
    with urlopen(url) as u:
        content = u.read().decode('UTF-8')
        with open('france.html', 'w', encoding='UTF-8') as f:
            f.write(content)

if __name__ == '__main__':
    main()
