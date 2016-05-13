#!/usr/bin/python
#programma uzziimee failaa 'burts_A.png' burtu 'A'

import numpy
from PythonMagick import Image

m = numpy.matrix([ \
[0,0,1,0,0], \
[0,1,0,1,0], \
[1,0,0,0,1], \
[1,0,0,0,1], \
[1,1,1,1,1], \
[1,0,0,0,1], \
[1,0,0,0,1], \
])
bilde = Image("5x7","#22aaff")

for i in range (0,5):
 for j in range (0,7):
  if(m[j,i]=1):
   bilde.pixelColor(i,j,"#FFF")
bilde.scale("200x200")
bilde.write("burts_A.png")
  
