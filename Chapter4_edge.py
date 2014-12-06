from scipy import misc 
from scipy.stats import norm
from skimage.filter import threshold_otsu
import matplotlib.pyplot as plt
import scipy.stats as st
import scipy.signal as sig
import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.557, 0.144])

def convolution(A,B):
	result=sig.convolve2d(A,B,'valid','fill',0)
	return result

def threshold(A,a,b):
	result=st.threshold(A,a,b,0)
	return result

def robertCross(A):
	robert_minus=np.array([[1,0],[0,-1]])
	robert_plus=np.array([[0,1],[-1,0]])
	result1=convolution(A,robert_minus);
	result1=np.abs(result1)
	thresh1=np.floor(threshold_otsu(result1))
	result1=np.logical_or(result1<0,result1>thresh1)
	result2=convolution(A,robert_plus);
	result2=np.abs(result2)
	thresh2=np.floor(threshold_otsu(result2))
	result2=np.logical_or(result2<0,result2>thresh2)
	result=np.logical_or(result1,result2);
	return result
	
def prewitt(A):
	edge_y=np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
	edge_x=np.array([[1,0,-1],[1,0,-1],[1,0,-1]])	
	result1=convolution(A,edge_x);
	result2=convolution(A,edge_y);
	result=np.sqrt(np.square(result1)+np.square(result1))
	return result;
	
def sobel(A):
	edge_y=np.array([[1,2,1],[0,0,0],[-1,-2,-1]])
	edge_x=np.array([[1,0,-1],[2,0,-2],[1,0,-1]])	
	result1=convolution(A,edge_x);
	result2=convolution(A,edge_y);
	result=np.sqrt(np.square(result1)+np.square(result1))
	return result;	
	
if __name__=='__main__':
	lena=misc.lena()
	#lena=rgb2gray(lena)
	rows,cols=lena.shape
	print(rows,cols)
	order1diff=np.array([[2,-1],[-1,0]])
	order1edge=convolution(lena,order1diff)
	plt.imshow(order1edge,cmap=plt.cm.gray)
	plt.show()
	robertedge=robertCross(lena)
	plt.imshow(robertedge,cmap=plt.cm.gray)
	plt.show()
	prewittedge=prewitt(lena)
	plt.imshow(prewittedge,cmap=plt.cm.gray)
	plt.show()
	sobeledge=sobel(lena)
	sobelthresh=np.floor(threshold_otsu(sobeledge))
	sobeledge=np.logical_or(sobeledge<0,sobeledge>sobelthresh)
	plt.imshow(sobeledge,cmap=plt.cm.gray)
	plt.show()
