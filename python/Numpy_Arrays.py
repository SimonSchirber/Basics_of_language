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



# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
a = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3] #[[2 3][6 7]]


#Array math
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Elementwise sum; both produce the array
print(x + y)
print(np.add(x, y))

# Elementwise difference; both produce the array
print(x - y)
print(np.subtract(x, y))

# Elementwise product; both produce the array
print(x * y)
print(np.multiply(x, y))

# Elementwise square root; produces the array
# [[ 1.          1.41421356]
#  [ 1.73205081  2.        ]]
print(np.sqrt(x))

# Dot Product vectors
print(x.dot(y))
print(np.dot(x, y))
print(x @ y)

# Matrix / vector product; both produce the rank 1 array [29 67]
print(x.dot(y))
print(np.dot(x, y))
print(x @ 7)