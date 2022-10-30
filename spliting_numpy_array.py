import numpy as np
#Spliting is reverse operation of numpy array
#Spliting an 1d array usung split() method it take stwo pararmeter the array itself which goin to splited
#Another one is number division is need this is important it takes equal divisional
#if Array contains 6 element so the possible division would be 2 or 3 if we try to give 4 or 5 then it give an error casue 4 or 5 is divided by 6
arr = np.array([10,25,6894,6464,694,616,16,161])
split_arr = np.split(arr,4)
print(f"The Main Array is \n{arr}")
print(f"The splited Array of Main Array Is \n{split_arr}")

# To Avoid Issues From Lne 3-5 We Can Use array_split() method
# Which Will Handle The Divisional error and we can automatical adjust the unequal division se the exmple below
split_arr_i = np.array_split(arr,3)
print(f"Unequal Deivision of Main Array is\n{split_arr_i}")

#We Can Also split 2D Array By Using array_split()

arr2 = np.array([[12,548,874],[894,1456,516],[16,61,25],[56,165,98],[74,84,59],[41,54,56]])
new_arr_2D = np.array_split(arr2, 3,axis =1)
print(f"The 2D Array is Which Going to Be Splited is \n{arr2}")
print(f"New 2D Array Which Divided into 3 part From Array 3 Row By Row is \n{new_arr_2D}")
new_arr_2D_0 = np.array_split(arr2, 3,axis =0)
print(f"New 2D Array Which Divided into 3 part From Array 3 col By col is \n{new_arr_2D_0}")