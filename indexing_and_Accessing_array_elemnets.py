import numpy as np
arr = np.array([1,2,3,4,5,9])
#Getting The 4 the elements From the Array As It its index start from 0 The third element would in index 3
print(arr[3])

# Addintion 2nd and 5th elemenT Would be
print('\n')

print(arr[1] + arr[4])

#Accessing 2D Array
#2D Array Has 2 dimension Which Is Row and Column Syntax For Accesing 2D array Element of array[[]] is array[row][col] where first outer last outer [] defins row and first [ inside last inside ] defines col

arr2 = np.array([[1,2,3,4],[5,6,7,8]])

# Access 3rd element of first Row And Access 2nd elemnt of second Row Would be
print('\n')
print('A 2D array is \n',arr2)
print("3rd element of first row of the above 2d Array is",arr2[0,2])
print("2nd element of second row of the above 2d Array is",arr2[1,1])

#Accessing 2D Array
#3D Array Has 3 dimension Which which is separtaed by set of 2d array and each 2d array contains 2 array so to access elemnet we need first specify set of 2d
#Then we have to specify the 2d array accese as arry[row][col] or array [row,col] so the total would be array [index set of 2d array,index of the 2d array row,  index of 2d array colounm]

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print('\n')
print("A 3D Arrray Is \n",arr3)
#Accesing Second Element of the 1st  2d array which 5
print("Second element of the 1st  2d array of 3d array above is  ",arr3[0,1,1])
#Accesing Last  Element of the 3rd  2d array which 18
print("Last  element of the 3rd  2d array of 3d array above is  ",arr3[2,1,2])

