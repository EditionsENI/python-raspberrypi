#!/usr/bin/env python3
def obtenir_temperature():
    with open('/sys/class/thermal/thermal_zone0/temp') as t:
        temp = t.read()
    return int(temp) / 1000

print('Content-Type: text-html; charset=utf-8\r\n\r\n')
print("""
<html>
<head>
<title>Exemple #2: Formatter du code HTML directement en Python</title>
</head>
<body>
  <h1>Obtenir des informations en temps r&eacute;el</h1>
  <p>Temp&eacute;rature actuelle du processeur du Raspberry Pi: %s C</p>
</body>
</html>""" % (obtenir_temperature()))
