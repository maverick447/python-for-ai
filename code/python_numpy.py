import numpy as np
arr = np.array([1,2,3])
print(type(arr))
print(arr)

# convert the numpy to list 
array = arr.tolist()
print(array)
print(type(array))

# convert the list to an numpy.ndarray
arr = np.array(array)
print(arr)
print(type(arr))
# you cannot make this array non-homogeneous 
#arr = np.array([(1,2,3, 'sad', 3.5, False),(4,5,6, 6.5, 'ass')])
# the statement has mix of variables first integer, then flat and finaaly a boolean 
# Converted to float [[1.  2.  3.  3.5 0. ]
# [4.  5.  6.  6.5 0. ]]
#arr = np.array([(1,2,3, 3.5, False),(4,5,6, 6.5, False)])
# even works if strings are used 
#arr = np.array([('ab','bc'),('cd', 'de')])
arr = np.array([[1,2,3,4],[5,6,7,8]], np.int8)
print(type(arr))
print(arr)

# shape of the array
arr.shape
# d type 
arr.dtype
# convert the numpy to list 
array_array = arr.tolist()
print(array_array)
print(type(array_array))

array_1 = array_array[0]
array_2 = array_array[1]
print(array_1)
print(array_2)

for i in array_1:
    print(i)
    print(type(i))
    
for i in array_2:
    print(i)
    print(type(i))    
# convert the list to an numpy.ndarray
arr = np.array(array_array)
print(arr)
print(type(arr))

# use of the array 
print(arr[0,0])
print(arr[0,1])

print(arr[1,3])

array_1 = arr[:,1]
print(array_1)

array_1 = arr[:,0]
print(array_1)