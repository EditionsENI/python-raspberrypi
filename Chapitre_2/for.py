#!/usr/bin/env python3
liste = [1, 2, 3, 4, 5]

for element in liste:
    if element == 2:
        continue
    if element == 4:
        break
    print("element = " + str(element))
