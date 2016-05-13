#!/usr/bin/python
import numpy
from PythonMagick import Image

bilde = Image("400x400","#22aaff")

for j in range(1,400):
  for k in range(1,400):
      if (j**2+k**2>400**2):
        bilde.pixelColor(j, k, "#FFF")

bilde.write("circle.png")
  
