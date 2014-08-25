from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

#lena=misc.lena()
lena=misc.imread("geoaware1.jpg",1)
#manipulating individual pixel values
#lena[100:150]=255
#lena[100:150,100:120]=255

#printing values of pixels
#print lena[100:103, 20:23]

#different color schemes-- gray, hot, summer, spectral,Blues,Greens.. etc
plt.imshow(lena,cmap=plt.cm.gray)
plt.colorbar() 

#plt.imshow(lena);
#plt.show()
lx,ly=lena.shape
#print lx,ly
X,Y= np.ogrid[0:lx,0:ly]
#print Y.shape,X.shape

#masking
#mask=(X-lx/2)**2 + (Y-ly/2)**2 >lx*ly/4
mask=(X-lx/2)**2 + 2*(Y-ly/2)**2 >lx*ly/4
lena[mask]=0;

#lena[range(400),range(100,500)]=255;
plt.show() 
