import numpy as np
arr1 = np.array([10,52,69,74,84,94,646,564561,65])
#Iteration Over The Arr1 Using For loop Will Be :

for items in arr1:
    print(items)#It will Print Every Single item one by one of the array


print('\n')

#Iteration Over The  A 2D Array Arr2 Using For loop Will Be :
arr2 =np.array([[12,548,874,894,1456,516,16,61],[56,165,98,74,84,59,41,54]])

for items in arr2:
    print(items)# Will Print The Inner Array Which Arae [12,548,874,894,1456,516,16,61],[56,165,98,74,84,59,41,54] separated inside [[12,548,874,894,1456,516,16,61],[56,165,98,74,84,59,41,54]]
    for item in items:
        print(item)#it will print the element inside array one by one from [12,548,874,894,1456,516,16,61] and From [12,548,874,894,1456,516,16,61]

print('\n')
#Iteration Over The  A 3D Array Arr2 Using For loop Will Be :

arr3 = np.array([[[154,59,694,97,4,],[654,564,64,46,874]],[[1,236,54,564,14],[56,145,659,65,84]],[[996,94,645,94,4],[10,11,25,65,46]]])
for items in arr3:
    print(items)#This Will Print each  three inner array
    print('\n')
    for item in items:# this print The each single array from 2d array gotten from the 2d array at line 24
        print(item)
        print('\n')
        for element in item:
            print(element)#This will print the each rayya elemnt one by on egotten from the line 27-28


#We can Avoid nested loop Using nditer() method
print('\n')
print("Used nditer() Method Syntax np.nditer(Array)")
arr4 = np.array([[[154,59,694,97,4,],[654,564,64,46,874]],[[1,236,54,564,14],[56,145,659,65,84]],[[996,94,645,94,4],[10,11,25,65,46]]])

for element in np.nditer(arr4):
    print(element)
print("\n")
#We can Also change the Data Type Of the Array While Iterating Using nditer() method Just ween need pass op_dtypes = 'Choice of your a data type' parameter inside the nditer() method
arr5 = np.array([10,20,50,90,70,80,50,90,100])
for element in np.nditer(arr5, flags=['buffered'], op_dtypes='S'):# here flags works like (NumPy does not change the data type of the element in-place (where the element is in array) so it needs some other space to perform this action, that extra space is called buffer, and in order to enable it in nditer() we pass flags=['buffered'].)
    print(element)

#Enumerated Iteration Using ndenumerate()
#Enumeration means mentioning sequence number of somethings one by one.

print('\n')
arr6 = np.array([10,20,50,90,70,80,50,90,100])
for index,element in np.ndenumerate(arr6):
    print(index,element)

print('\n')
#Enumeration on a 2D array
arr7 = np.array([[10,20,50,90,70,80,50,90,100],[10,30,505,48,758,885,5560,95640,5600]])
print(f"Enumeration on a 2D array \n{arr7}\n")
for index,element in np.ndenumerate(arr7):
    print(index, element)