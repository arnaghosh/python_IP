from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

lena=misc.lena()

lx,ly=lena.shape

cropped_lena= lena[lx/4:-lx/4 , ly/4:-ly/4]
print cropped_lena.shape
plt.imshow(cropped_lena,cmap=plt.cm.gray)
plt.show()
