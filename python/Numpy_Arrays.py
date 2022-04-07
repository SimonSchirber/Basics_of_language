import numpy as np

#single element array
a = np.array([1, 2, 3])

# Rank two array, [notice outside brackets]
b = np.array([[1, 2, 3], [4, 5, 6]])

print(b.shape) #(2,3) This has two elements with a length of three
print((b[1,0])) #4. Print the index one elements 0 index

#initialize array of zeroes (2 by 2 array)
z = np.zeroes((2,2))

#initialize array of ones (2 by 2 array)
o = np.ones((2,2))

#initialize array with constant (of 7's) (2 by 2 array)
s = np.full((2,2), 7)

#initialize 2x2 identity matix (1's from top right to bottm left)
i = np.eye(2)

#initialize random number filled array (2 by 2 array)
r = np.random.random((2,2))