import numpy as np
#Joins In Numpy Means Concatnating two ror mare numpy array
"""
In NumPy we join arrays by axes.
Where axe Stands for dimension of the array to join two or more numpy array each numpy array must have same dimension 
"""
#Below we will join tow numpy array into one array using numpy concatenate() arr1 arr2 both 1 dimensional array which shape is (0,4) mean 1 row 4 col which will return a single array
arr1 = np.array([12,52,64,58])
arr2 = np.array([25,56,9874,984])
joined_arr =np.concatenate((arr1, arr2))#Note concatenate() takes paramete as tupele  like (a,b)
print(f"Array 1 Is {arr1}")
print(f"Array 2 Is {arr2}")
print(f"Joined Array of Array 1 and Array 2 is {joined_arr}")
print("\n")
#Below we will join two  2d numpy array into one array using numpy concatenate() arr3 arr4 bothare  2 dimensional array which shape is (4,4) which means 4 row 4 col which will return a single 2d array
arr3 = np.array([[12,52,64,58],[25,56,9874,984],[45,856,89,74],[54,684,84,947]])
arr4 = np.array([[10,256,369,48],[5,664,494,64],[60,50,54,64],[5454,64,6464,64]])
'''
Note For Concaneting 2D Array using concatenate() with axis parameter
if we want join the array row by row we can use axis = 0 or for joining the array by column to olumn we have to use axis =1 
'''

print("\n")
joined_arr2 =np.concatenate((arr3, arr4), axis =0)
print(f"Array 3 Is \n{arr3}")
print(f"Array 4 Is \n{arr4}")
print(f"Joined Array of Array 3 and Array 4 with axis = 0 is\n {joined_arr2}")
print("\n")
joined_arr2_1 =np.concatenate((arr3, arr4), axis =1)
print(f"Array 3 Is \n{arr3}")
print(f"Array 4 Is \n{arr4}")
print(f"Joined Array of Array 3 and Array 4 with axis = 1 is \n{joined_arr2_1}")
#Creating 2D Array Using Stack() Method With Passing axis  for axis understandinf see line 20to define how make the 2d array
arr5 = np.array([12,549,97,64,6])
arr6 = np.array([13,25,6816,65,4])
new_joined_arr_2D = np.stack((arr5,arr6),axis=0)
print('\n')
print(f"Array 5 is 1d Array Which  is {arr5}")
print(f"Array 6 is 1d Array Which  is {arr6}")
print(f"Joined Array Of Array 5 And 6 Will Be a 2D Cause used Stack() With Axis =0 Which Will join The Array row to row which is \n{new_joined_arr_2D}")
new_joined_arr_2D_1 = np.stack((arr5,arr6),axis=1)
print(f"With Axis =1 Which Will join The Array col  to col which is \n{new_joined_arr_2D_1}")