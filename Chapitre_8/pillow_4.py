#!/usr/bin/env python3
from PIL import Image
image = 'images/hello_1.png'
resultat = 'images/hello_4.png'
img = Image.open(image)
nouvelletaille = (100, 0, 300, 200)
res = img.crop(nouvelletaille)
res.save(resultat)
