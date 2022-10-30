import numpy as np
"""
Slsicing mean diving the Array Using Index Into Another Portion 
Syntax for Slicing Is Array[Start:End] And [start:end:step]
Where start indicates first index to start indexing and end indcates where the indexing will stop and step mean interval 
By default start index 0 and end index is lenght of the array 
"""
arr = np.array([154, 254,122, 54, 89, 47, 90])
#Slicing The abve array from 1 to 5the element which means it will start from 254 to end to 89
# cause end workrs like n-1 where n is the 5 so end will be 5-1 = 4 yhe 4th element in the array is 5
print("The To be Sliced\n ",arr)
print("Slicing of The  Above Array to 1:5 \n",arr[1:5])
#slicing The Array From 3 index to the End of The Array Would be [3:] As It has only starting Index and It Does Not have ending index the ending index would be the lenght of the array
# and the result WUld be from 54 to 90
print("Slicing of The  Above Array from 3:end  \n",arr[3:])
#slicing The Array From stat  index to the 5 of The Array Would be [:6] As It has no  starting Index so it woul be  0 ending index is 5 which menan  n-1 = 6-1 = 5
# so the last elemnet of the sliced array would be 5th element of the array which is 47
# so Sliced array would be 154 to 47
print("Slicing of The  Above Array from :6  \n",arr[:6])

#Slicing 2D Array

arr2 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#To Slicing 2D Firsty Wee Need to Specify the index Of The row Then The as usual The slicing syntax
#So The Real scenario would be array[row,start:end]
#slicing the arr2 second row from 2 to 5 that means arra2[1,2:5] which will start from 2 ends to 4 as end = n-1=5-1=4 4 th index
#result will be 8 to 10
print("A 2d Array Is \n",arr2)
print("Sliced the Second array to 2:5  Of The Above 2D Array is ",arr2[1,2:5])

#To Get Same Element From The Both Arrays In 2D Array
#We First need Slice The Row Then The Specify The Index of the element like array[(slicing the row), indexof the element inside evry row] like array[O:n-1,n]

arr3 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[15, 58, 78, 25,41],[56, 89, 78, 89,101]])
#Retrivng every elemnet at index 3 from second to last array of the arr3 2d array
#The syntax would be arr3[1:4,3] as the 2d has 4 set of array  so the last array would in postion 3 which equal to n-1 =4-1=3
# The result will a set of array 9,25,89
print("A 2d Array Is \n",arr3)
print("Slicing the as it will create a set 3rd elemnt of the array range from 1:4 from the above array ",arr3[1:4,3])


