#!/usr/bin/env python3
from PIL import Image
image = 'images/hello_1.png'
resultat = 'images/hello_3.png'
nouvelletaille = (300, 150)
img = Image.open(image)
res = img.resize(nouvelletaille)
res.save(resultat)
