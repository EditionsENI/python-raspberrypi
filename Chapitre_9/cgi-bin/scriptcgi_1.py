#!/usr/bin/env python3
import datetime
print('Content-Type: text-html; charset=utf-8\r\n\r\n')
html = """
<html>
<head>
<title>Exemple #1: Simple programme "Hello world" en CGI</title>
</head>
<body>
  <h1>Hello Pi CGI!</h1>
  <p>Cette page est g&eacute;n&eacute;r&eacute;e &agrave; l'aide d'un script CGI &eacute;crit en Python.<p>
  <p>Requ&ecirc;te &eacute;ffectu&eacute;e &agrave;: %s</p>
</body>
</html>""" % (
    datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f"),
)
print(html)
