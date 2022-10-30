import numpy as np
"""
Data Types Of Numpy Array Are 
Below is a list of all data types in NumPy and the characters used to represent them.

i - integer
b - boolean
u - unsigned integer
f - float
c - complex float
m - timedelta
M - datetime
O - object
S - string
U - unicode string
V - fixed chunk of memory for other type ( void )
"""
#Chekeing Numpy Array Data Type Using dtype attribute
arr = np.array([1, 2, 3, 4])
arr2 = np.array(['a', 'b', 'c', 'd'])
arr3 = np.array([True, False, False, True])
print(f"Array 1 is {arr} its Data Type is {arr.dtype}")
print(f"Array 2 is {arr2} its Data Type is {arr2.dtype}")
print(f"Array 3 is {arr3} its Data Type is {arr3.dtype}")

#Creating Array with Definig The Data Type By Setting The Paramete dtype ins array() method

arr4 = np.array([1, 2, 3, 4],dtype=float)
print(f"Array 4 is {arr4} its Data Type is {arr4.dtype}")

#Converting Data Type Of An Exiting Array By Using astype method which take parameter like from the line 6-16

arr5 = np.array(['1','2','3','4'])
print(f"Array 5 is {arr5} its Data Type is {arr5.dtype}")
print("After Converting The Array 5 to Int It Would Be Like Below")
arr5 = arr5.astype('i')
print(f"Now Array 5 is {arr5} its Data Type is {arr5.dtype}")

