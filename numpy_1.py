import numpy as np
#Creating 1D Array
array1 = np.array([1,2.,3,4,5,6])
print(array1)

print('\n')

#Crerating 2D Array

array2 = np.array([[1,2,3,4],[5,6,7,8]])
print(array2)

print('\n')
#Creating 3d array

array3 = np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(array3)

#Check Dimension Of At Array using ndim Attribute of numpy

print(f"The Dimension of Array 1 is {array1.ndim}")
print(f"The Dimension of Array 2 is {array2.ndim}")
print(f"The Dimension of Array 3 is {array3.ndim}")

#A numpy array can any of number of dimension lets create a 7 dimension of numpy array or so called ndarray vice versa
# The array takes ndim parameter also
array4 = np.array([1,2,3,4,5], ndmin=7)

print('\n')
print("This is a 7 Dimensional Array\n",array4)
print(f"The Dimension of Array 4 is {array4.ndim}")