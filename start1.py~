from scipy import misc
l = misc.lena()
misc.imsave('lena.png', l) # uses the Image module (PIL)

lena = misc.imread('lena.png')
print type(lena), lena.shape, lena.dtype

import matplotlib.pyplot as plt
plt.imshow(l,cmap=plt.cm.gray)
plt.show()
#plt.imshow(l,cmap=plt.cm.gray,vmin=30,vmax=200)
#plt.show()
plt.imshow(l,cmap=plt.cm.gray,vmin=60,vmax=200)
plt.show()
#plt.imshow(l,cmap=plt.cm.gray,vmin=30,vmax=100)
#plt.show()
plt.contour(l,[30,200])
plt.show()
