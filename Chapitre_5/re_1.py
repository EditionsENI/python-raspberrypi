#!/usr/bin/env python3
import re

pattern = re.compile('^.*bash$')
for ligne in open('/etc/passwd', 'r'):
    ligne = ligne.strip()
    if pattern.match(ligne):
        print(ligne)
