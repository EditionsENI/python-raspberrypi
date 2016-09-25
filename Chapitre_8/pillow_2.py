#!/usr/bin/env python3
from PIL import Image
image = 'images/hello_1.png'
resultat = 'images/hello_2.png'
rotation = 90
img = Image.open(image)
res = img.rotate(90)
res.save(resultat)
