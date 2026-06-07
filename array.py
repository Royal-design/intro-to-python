from array import *
list = [1,2,3,4]
arr1 = array('i',list)
print(type(arr1))

for n in arr1:
    print(n)

arr1.append(21)
print(arr1.tolist())

