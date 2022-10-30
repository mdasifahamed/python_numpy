import numpy as np
#Searching numpy array elemnet findig out an element index or by giving index finding out the elemnet in the array
#using where() method we can find element index if it exist in th earray
arr = np.array([10,52,556,561,6146,61,62])
x = np.where(arr==61)
print(x)
# If We Have Same Element in The Multiple Positions in the it will return the al the index where the element exits
arr2 = np.array([10,52,556,561,6146,61,62,10,6051,641061,10,5651,64616,659,94,461,10])
y = np.where(arr2==10)
print('\n')
print(f"Array to fiind Elements 10 indexs is \n{arr2}")
print('\n')
print(f" 10 Are in the Above Array position {y}")
print("\n")

"""
There Is Functions Called searchsorted() Which uses binary serch and the The Element 
We can Search for Muttiple values using this function
it will return first position aftersorting the value has multiple times 
and this array aslo take the array it as parameter too

"""
#seraching single value
arr3 = np.array([10,52,556,561,6146,61,62,10,6051,641061,10,5651,64616,659,94,461,10])
z = np.searchsorted(arr,10)
print('\n')
print(f"Array to find Elements 10 indexs is \n{arr3}")
print('\n')
print(f" 10 Are in the Above Array position {z}")
print("\n")
#seraching multiple value  value
arr4 = np.array([10,52,556,561,6146,61,62,10,6051,641061,10,5651,64616,659,94,461,10])
s = np.searchsorted(arr,[556,5651,61,461])#To search Multiple values  We have passed the value as list
print('\n')
print(f"Array to find Elements  indexs is \n{arr4}")
print('\n')
print("Item will be Searched are 556,5651,61,461 From the above Array")
print(f"Positions  Of The Avobe Elements in The Array Are {s}")
print("\n")
