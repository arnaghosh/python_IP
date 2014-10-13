from scipy import misc 
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.557, 0.144])

def histogram(gray):
	hist,bin_edges=np.histogram(lena,range=(0,255))
	return hist,bin_edges
	
def normalisation(gray,nmin,nmax):
	omax=np.amax(lena)
	omin=np.amin(lena)
	conv=(nmax-nmin)*1.0/(omax-omin)
	lena2=gray.copy()
	lena2=conv*(lena-omin) + nmin
	return lena2		
	
def binary_search(intList, intValue, lowValue, highValue):
    if(highValue - lowValue) < 2:
        return intList[lowValue] == intValue or intList[highValue] == intValue
    middleValue = lowValue + ((highValue - lowValue)/2)
    if intList[middleValue] == intValue:
        return True
    if intList[middleValue] > intValue:
        return binary_search(intList, intValue, lowValue, middleValue - 1)
	return binary_search(intList, intValue, middleValue + 1, highValue)

if __name__=="__main__":
	lena=misc.imread("lena.png")
	#lena=rgb2gray(lena)
	print(lena.shape)
	plt.imshow(lena,cmap=plt.cm.gray)
	plt.show()
	rows,cols = lena.shape
	nmin=50
	nmax=250
	new_range=nmax-nmin
	number_of_pixels=rows*cols
	omax=np.amax(lena)
	omin=np.amin(lena)
	print(omax,omin)
	print(nmax,nmin)

	#histogram creation....
	hist=np.array([0 for i in range(256)])
	hist,bin_edges=histogram(lena)
	plt.hist(lena.flatten())
	plt.show()
	plt.plot(hist)
	plt.show()

	#histogram normalisation... to 50->200

	lena2=normalisation(lena,nmin,nmax)
	newmin=np.amin(lena2)
	newmax=np.amax(lena2)
	print(newmin,newmax)
	plt.imshow(lena2,cmap=plt.cm.gray)
	plt.show()
	hist_size=hist.size
	print(hist_size)

	#histogram equalisation


	hist2=np.array([0 for i in range(256)])
	psum=np.cumsum(hist)
	print(bin_edges)
	print((new_range*1.0*psum[0])/number_of_pixels)
	for i in range(256):
		for j in range(hist_size):
			if(i<=bin_edges[j]):
				hist2[i]=(new_range*1.0*psum[j-1])/number_of_pixels
				break

	plt.plot(hist2)
	plt.show()
	lena3=lena.copy()
	for i in range(rows):
		for j in range(cols):
			lena3[i,j]=hist2[lena[i,j]]
	plt.imshow(lena3,cmap=plt.cm.gray)
	plt.show()
	hist2_,bin_edges2_=histogram(lena3)
	plt.plot(hist2_)
	plt.show()
	hist,bin_edges=histogram(lena)
	plt.plot(hist)
	plt.show()
	print("eq done")

	#OTSU thresholding

	w=np.array([0.00 for i in range(256)])
	w[0]=(hist[0]*1.0)/number_of_pixels
	for i in range(255):
		w[i+1]=w[i]+(hist[i+1]*1.0)/number_of_pixels 

	mu=np.array([0 for i in range(256)])
	mu[0]=1*hist[0]*1.0/number_of_pixels
	for i in range(255):
		mu[i+1]=mu[i]+((i+2)*hist[i+1]*1.0)/number_of_pixels

	muT=mu[255]

	#plt.plot(w)
	#plt.show()
	thresh=0
	maxValue=0
	for i in range(256):
		if(w[i]==0):continue
		val=(muT*w[i]-mu[i])*(muT*w[i]-mu[i])/(w[i]*(1.0-w[i]))
		if(val>maxValue):
			maxValue=val
			thresh=i

	print(thresh)
	lena4=lena.copy()
	for i in range(rows):
		for j in range(cols):
			if(lena[i,j]>=thresh):lena4[i,j]=255;
			else : lena4[i,j]=0;

	plt.imshow(lena4,cmap=plt.cm.gray)
	plt.show()
