#!/usr/bin/env python3
from PIL import Image, ImageOps
image = 'images/hello_1.png'
resultat = 'images/hello_5.png'
img = Image.open(image)
res = ImageOps.flip(img)
res.save(resultat)
