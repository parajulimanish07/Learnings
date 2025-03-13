#NUMPY - library that allows us to work with vectors, matrices, and arrays in Python 
# basis for most data science and ML libraries.

import numpy as np

#Numpy arrays
# a = np.array([1,2,3,4,5])

# print(a)
# print(a[:-2]) #slicing

# a_mul= np.array([[[1,2,3],
#                 [4,5,6],
#                 [7,8,9]],
#                 [[1,1,1],
#                  [2,2,2],
#                  [3,3,3]]])

# print(a_mul.shape)
# print(a_mul.ndim) #dimension dincha esle
# print(a_mul.size)
# print(a_mul.dtype) #data type
# print(a_mul.itemsize) #size of each element in bytes

# d = {'1': 'A'} #dictionary
# a = np.array([[1,2,3],
#               [4,d, 6],
#               [7,8,"hello"]]) 
# print(a.dtype) #data type - object
# print(type(a[1][0]))


# a = np.full((2,3,4), 9) #array filled with same elements
# print(a)

# a = np.empty((5,5,5)) #np.empty() is a function in NumPy that creates an array without initializing its values.
# This means the array is created with a specific shape, but the values inside it are random or whatever was already in memory.
# It’s like getting a blank piece of paper with random scribbles on it—you don’t know what’s there until you write on it.

# a = np.zeros((2,3,4)) #array filled with zeros



# x_values = np.arange(0, 1000, 5) #arange - start, stop, steps
# print(x_values)

#linspace

# x_values = np.linspace(0, 1000, 1000) #linspace - start, stop, number of elements
# print(x_values)


# print(np.nan) #np.nan stands for "Not a Number". It’s used to represent missing or undefined values in your data.
# print(np.inf) #np.inf stands for infinity. It’s used to represent positive or negative infinity in your data. #division by zero

# print(np.sqrt(-1)) 
# print(np.array([10])/0) 