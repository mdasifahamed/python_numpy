import numpy as np
"""
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view.

"""
#Copying an Array means Creating a New Object Array From The array object That has been copied
#Creating an Copy of Array Using copy() method
arr = np.array([1, 2, 3, 4, 5])
arr_c = arr.copy()
print(f"Main Array is {arr}")
print(f"Copied Array is {arr_c}")

"""
Now If We Change Anything on the Copied array it will not affect the Original array 
now if we change an element on the arr_c the no change  will be on the main arr see the example below
"""
#Changing index three element with three
arr_c[3] = 6
print(f"After changing To Copy The Main Array is {arr}")
print(f"After changing To Copy The Copy Array is {arr_c}")

"""
View Is Temporaray If We Create A View An array And Make Some Change On the Array That Has Been Made By The view 
It Change THe Original Array
"""
print('\n')
#Create A View using view()
arr2 = np.array([12,52,56,58,78,97])
arr_v = arr2.view()
print(f"Main Array is {arr2}")
print(f"View of the  Array is {arr_v}")

#Now Changing Element on th index number 4 to 100 on the view array it will result the changing the main array also
arr_v[3] = 100

print("\n")
print("After Changing tot view array arr_v[3]=10")
print(f"Main Array is {arr2}")
print(f"View of the  Array is {arr_v}")

