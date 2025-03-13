import numpy as np

# a1 = np.array([1,2,3])
# a2 = np.array([[1],[2]])

# print(a1 + a2)

# # print(a1 * 5) #l1 *5 le 5 times dekhaucha whereas a1 * 5 le multiply garera dekhaucha

# print(l1 + l2) #unsupported except addition
# print(a1 / a2)


# a = np.array([[1,2,3],
#                [4,5,6]])

# print(np.log10(a))

# a = np.array([[1,2,3,4,5],
#              [6,7,8,9,10],
#              [11,12,13,14,15],
#              [16,17,18,19,20]])


# a = np.append(a, [7,8,9])
# a = np.insert(a, 3, [4,5,6])
# print(np.delete(a,1, 1)) #row ra column delete garna milcha

# print(a.shape)
# print(a.reshape(5,4))
# print(a.reshape(20,))
# print(a.reshape(2,10))
# print(a.reshape(2,2,5))
# print(a.reshape(2,5,2))
# print(a.reshape(5,2,2))

# a.resize((10,2))
# print(a)

# print(a.flatten()) #flatten copy 
# print(a.ravel()) #change actual values


# var = [v for v in a.flat]
# print(var)

#TRANSPOSING AND SWAPPING 
# print(a.T) #transpose all axes

# print(a.swapaxes(0,1)) #swapaxes - pick two axes to swap

# a1 = np.array([[1,2,3,4,5],
#              [6,7,8,9,10]])
# a2 = np.array([[11,12,13,14,15],
#             [16,17,18,19,20]])

#CONCATENATE AND STACK
# a = np.concatenate((a1, a2), axis=1)
# print(a)

# a =np.hstack((a1, a2)) #stack helps to stack arrays along a new axis

#SPLIT

a = np.array([[1,2,3,4,5,6],
             [6,7,8,9,10,11],
            [11,12,13,14,15,16],
            [16,17,18,19,20,21]])

# print(np.split(a,6,axis=1))

#AGGREGATE FUNCTIONS

# print(a.min())

# number = np.random.randint(90,100, size=(2,3,4))
# numbers = np.random.binomial(10, p=0.5,size=(5,10))
# numbers = np.random.normal(loc=170, scale=15,size=(5,10))

# numbers = np.random.choice([10,20,30,40,50], size=(5,10))

# np.save("MyArray.npy", a)
# np.savetxt("MyArray.csv", a, delimiter=",")

a=np.loadtxt("myarray.csv", delimiter=",")
print(a)

# print(numbers)