#!/usr/bin/env python3
import subprocess
commande = 'df -h'
print('Espace disponible:')
proc = subprocess.Popen(commande.split(' '), stdout=subprocess.PIPE)
out_cmd = proc.communicate()[0]
out_cmd = out_cmd.decode('UTF-8')
for ligne in out_cmd.split('\n'):
    print(ligne.strip())
