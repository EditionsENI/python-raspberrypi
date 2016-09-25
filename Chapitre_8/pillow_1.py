#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageFont
import os

if not os.path.exists('images'):
    os.mkdir('images')
texte = 'Hello world avec Pillow'
tailleimage = (600, 300)
font = ImageFont.truetype(filename='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', size=20)
img = Image.new(mode='RGB', color=(0, 110, 145), size=tailleimage)
drawer = ImageDraw.Draw(img)
tailletexte = drawer.textsize(texte, font)
drawer.text((
    (tailleimage[0] - tailletexte[0]) // 2,
    (tailleimage[1] - tailletexte[1]) // 2
    ),
    text=texte, fill=(255, 255, 255), font=font
)
img.save('images/hello_1.png')
