#!/usr/bin/env python3
from PIL import Image, ImageDraw, ImageOps
import os
if not os.path.exists('resources'):
    os.mkdir('resources')

img = Image.new('RGBA', (100, 100))
draw = ImageDraw.Draw(img)
draw.ellipse((25, 25, 75, 75), fill='red')
img = img.resize((25, 25))
img.save('resources/enreg.png')

img = Image.new('RGBA', (100, 100))
draw = ImageDraw.Draw(img)
draw.polygon([(25, 50), (75, 25), (75, 75)], fill='black')
img = ImageOps.mirror(img)
img = img.resize((25, 25))
img.save('resources/lire.png')

img = Image.new('RGBA', (100, 100))
draw = ImageDraw.Draw(img)
draw.polygon([(25, 25), (75, 25), (75, 75), (25, 75)], fill='black')
img = img.resize((25, 25))
img.save('resources/stop.png')
