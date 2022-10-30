import numpy as np
#We Will Create A New FroM Filtering An Existing Array

arr = np.array([10,50,55,158,15,14,5,6,1035,15,20,60,41,542,610,55,0])
#Creating Array An Filtered Array That Contains Only Even Value From the Exiting Array arr

new_filtered_arr = []
for element in arr:
    if element%2==0:
        new_filtered_arr.append(element)
print(f"The Main Array is \n{arr}")
print(f"Filtered Array That Has been Made From Main Array  With Only Even Value is \n{new_filtered_arr}")
print('\n')
#Creating Array An Filtered Array That Contains values Which Are Greater than 100 not including 100
new_filtered_arr_1 = []
for items in arr:
    if items>100:
        new_filtered_arr_1.append(items)
print(f"Filtered Array That Has been Made From Main Array  With Values that only Greater Than 100 Excluding 100 is \n{new_filtered_arr_1}")
print('\n')
#Creating Array An Filtered Array That Contains values Which Are Smaller than 10  including 10
new_filtered_arr_2 = []
for item in arr:
    if item<=10:
        new_filtered_arr_2.append(item)
print(f"Filtered Array That Has been Made From Main Array  With Values that only Smamller  Than 10 including 10 is \n{new_filtered_arr_2}")
print('\n')