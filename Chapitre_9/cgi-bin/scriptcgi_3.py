#!/usr/bin/env python3
import cgi
formulaire = cgi.FieldStorage()
print('Content-Type: text-html; charset=utf-8\r\n\r\n')
html = """
<html>
<head>
<title>Exemple #3: Soumettre des formulaires avec la methode POST</title>
</head>
<body>
  <h1>Deuxieme &eacute;tape</h1>
  <p>%s<p>
</body>
</html>"""

if 'nom' in formulaire:
    print(html % ('Bonjour %s !' % formulaire['nom'].value))
else:
    print(html % 'Mais qui &ecirc;tes-vous !?')
