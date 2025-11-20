import numpy as np

data = np.array([[1,2,3],[4,5,6]])
print(data)
print(type(data))

# it is 3 d array like this 
'''
[[[0.18301306 0.58386287 0.43858121 0.72257793]
  [0.07946987 0.75116378 0.29408954 0.21179031]
  [0.13046756 0.86878535 0.10855087 0.31514881]]
 [[0.42078251 0.07721721 0.58785869 0.90534187]
  [0.18122541 0.67575193 0.39536675 0.94578249]
  [0.63223317 0.16603376 0.22554636 0.60631265]]]
'''
data = np.random.rand(2,3,4)
print(data)

data = np.random.rand(3,4,5)
print(data)

# this is single dimensions having 2 random floats
data = np.random.rand(2)
print(data)

# data of integers with randint 
# very different from np.random.rand functiom that can 
# create a random array for you
data = np.random.randint(1000)
print(data)

# zeroes 
# 1 -dimension
data = np.zeros(1)
print(data)
print(type(data))

# 1-dimension
data = np.zeros(2)
print(data)
print(type(data))

# 2-dimension
data = np.zeros((2,2))
print(data)
print(type(data))

# 2-dimension
data = np.zeros((3,3))
print(data)
print(type(data))

# full fills up array with value provided 
data = np.full(9)
print(data)
print(type(data))
# 2-d 
data = np.full((2,2), 9)
print(data)
print(type(data))

data = np.full((2,4), 9)
print(data)
print(type(data))

# ones all data pts are 1 
print(np.ones(12))

# ones all data pts are 1 
print(np.ones((3,3,2)))

# create an array 
print(np.array([1,3,5]))
#2-d 
print(np.array([[1,3,5,7],[0,2,4,6]]))
#3-d 
print(np.array([[[1,3,5,7],[0,2,4,6]]]))

data = np.array([[[1,3,5,7],[0,2,4,6]]],dtype=np.int8)
# reading from shape from numpy
shape = data.shape 
print('The shape of the array created is ', data.shape)
size = data.size
print(size)
types = data.dtype
print(types)

data = np.array([1,3,5], dtype=np.int16)
shape = data.shape 
print('The shape of the array created is ', data.shape)
size = data.size
print(size)
print(data.dtype)

data = np.array([[1,3,5,7,9],[0,2,4,6,8]])
shape = data.shape 
print('The shape of the array created is ', data.shape)
size = data.size
print(size)

data = np.array([[1,3,5,7,9],[0,2,4,6,8],[1,2, 3, 4, 5]])
shape = data.shape 
print('The shape of the array created is ', data.shape)
size = data.size
print(size)
print(data)
print(data[0])
print(data[0][1])
print(data[0][2])
print(data[1][0])
print(data[1][-1])

# slicing data 
arr = data[2]
print(arr)
# say we want to get the last value of 5 
integral_value = data[2][4]
print(integral_value)

# say we want to get the middle tuple and middle of 4 
integral_value = data[1][2]
print(integral_value)

slicer = data[0:2]
print(slicer)

slicer = data[0:3]
print(slicer)

slicer = data[0:4]
print(slicer)

slicer = data[2]
print(slicer)

# reversal 
reverse = data[-1]
print(reverse)

arr = np.array([1,3,5])
reverse = arr[-1]
print(reverse)

# update 
list1 = np.random.rand(5)
print("list1:", list1)
list2 = np.random.rand(5)
print("list2:", list2)

# basic math 
# addition of two arrays 
add = np.add(list1, list2)
print("Addition:", add)
print(len(add))
add = list1 + list2 
print("Addition:", add)

# Subration of two arrays 
sub = np.subtract(list1, list2)
print('Subtraction:', sub)

# division 
div = np.divide(list1, list2)
print("Division:", div)

# mul 
print("Multiply:", np.multiply(list1, list2))

# dot product (used for matrix multiplication)
print("Dot product:", np.dot(list1, list2))

a = [[1,2],[3,4]]
b = [[5,6],[7,8]]
#b = [[5,6], [7,8]]
print(a,b)
print("Dot product:", np.dot(a, b))

# Statistical functions 
print("Sqrt rt:",np.sqrt(14))
print("Abs value:", np.abs(-2))
print("power of 3^4:", np.power(3,4))
print("log of 25:", np.log(25))
print(f"Min of {a} = {np.min(a)}")
print(f"Max of {a} = {np.max(a)}")
print(f"Exponent of [2,3]: {np.exp([2,3])}")

# manipulation of data 
data = np.random.rand(2,3,4)
print(data)

data[0][0][0] = 3.14
print(data)

data[0][0][3] = 3.14
print(data)

data[1][0][0] = 1.0
print(data)

data[1][2][3] = 1.1
print(data)

# sorting data 
arr = np.array([5, 2, 8, 1, 9])
sorted_arr = np.sort(arr)
print(f"Original array: {arr}")
print(f"Sorted copy: {sorted_arr}")
sorted_desc = np.sort(arr)[::-1]
print(f"Reverse Sorting(h to l): {sorted_desc}")

# reshaping the array 
print(data.shape)
print(data)

# reshape it so that row = columns = 2 and the parameter as to what is the wish
data = data.reshape(2, 2, -1)
print(data.shape)
print(data)

# append values to the array created 
zeroes = np.zeros(8)
print(zeroes)

zeroes = np.append(zeroes, [2, 3, 4])
print(zeroes)

zeroes = np.append(zeroes, [[[2, 3, 4],[5,6,7],[8,9,10]]])
print(zeroes)

zeroes = np.zeros((3,3))
print(zeroes)

zeroes = np.append(zeroes, [[2, 3, 4],[5,6,7]], axis = 0)
print(zeroes)

zeroes = np.zeros((3,3))
print(zeroes)

# zeroes = np.append(zeroes,
#                     [
#                       [2, 3, 4],
#                       [5, 6, 7],
#                       [8, 9, 10]
#                     ],
#                   axis = 1)
# print(zeroes)

zeroes = np.append(zeroes, 
                    [
                      [2, 3, 4],
                      [5, 6, 7],
                      [8, 9, 10]
                    ],
                    axis=1)
print(zeroes)

zeroes = np.append(zeroes, [[[2, 3, 4],[5,6,7],[8,9,10]]])
print(zeroes)

# insert in the middle somwhere 
arr_1d = np.array([1, 2, 3, 4])
new_arr_1d = np.insert(arr_1d, 2, 99) # Insert 99 before index 2
print(new_arr_1d)
# Output: [ 1  2 99  3  4]

# deleting
data = np.random.rand(2,3,4)
print(data) 
# first row is deleted
np.delete(data, 0, axis=0)
print("Deletion is done horziontally due axis = 0")
print(data)

np.delete(data, 0, axis=1)
print("Deletion is done vertically due axis = 1")
print(data)

# saving the file
data = np.random.rand(2,3,4)
print(data) 
# first to a file  
np.save("new array", data)

# from a file 
test = np.load("new array.npy")
print(test)
