import numpy as np

# NumPy = Numeric Python
# nparray = a numpy array is a homogenous multidimensional array

# Creating a one-dimensional array
a = np.array([1, 2, 3])
# display(a) => array([1, 2, 3])
print(a)

# Creating a two-dimensional array with three rows and two columns
a = np.array([[1, 2],
              [3, 4],
              [5, 6]])
print(a)

# Creating a three-dimensional array with three rows and two columns
a = np.array([[[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]]])
print(a)

# Shap: .shape
print(a.shape)

# Important: NumPy distinguishes one-dimensional vectors and 2-dimensional matrices with 1 width or height
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3]])
print(a.shape, b.shape)

# Modifying the original object will not modify the array:
my_list = [1, 2, 3]
my_np = np.array(my_list)
my_list[0] = 0
print(my_list, my_np)

# np.arange
print(np.arange(3))
print(np.arange(1, 4))
print(np.arange(1, 11, 3))

# np.linspace
print(np.linspace(1, 13, num=5))

# np.random
# .rand = random numbers from a Uniform(low=0, high=1) distribution (-> mean around 0.5)
a = np.random.rand(10)
print(a)
print(np.mean(a))

# .randn = random numbers from a Normal(mean=0, var=1) distribution. (-> mean around 0)
b = np.random.randn(10)
print(b)
print(np.mean(b))

# .randint = random integer by default between 0 and the specified number.
print(np.random.randint(10))
print(np.random.randint(10, size=(2, 3)))
print(np.random.randint(10, 100, size=4))

# .permutation = random permutation of numbers.
print(np.random.permutation(10))
print(np.random.permutation(["one", "two", "three", "four", "five"]))

# np.ones, np.zeros,np.full
print(np.ones(4))
print(np.ones((2, 4)))
print(np.ones(4, dtype=bool))

print(np.zeros(4))
print(np.zeros((2, 4)))
print(np.zeros(4, dtype=bool))

print(np.full(4, 'rabbit'))

# Data types in NumPy arrays:
# A numpy array is homogenous (contains elements of the same type)
# unsigned integer types -> uint8, ..., uint64
# integers -> int8, ..., int64
# float types -> float8, ..., float32
# boolean types: bool
# string types: U6 -> for unicode string shorter than 6 chars
# a general Object type for arrays that can contain any python object

c = np.array([1, 2, 3], np.uint8)
print(c.dtype)
e = np.array([[1, 2, 3]])
print(e.dtype)
e = np.array([[1., 2, 3]])
print(e.dtype)
e = np.array([["12", 2, 3]])
print(e.dtype)

# .astype -> Change the dtype
a = np.ones(5)
print(a, a.dtype)
b = a.astype('bool')
print(b, b.dtype)

# Attributes of NumPy (Shape, Size, ...)
a = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, 10, 11]])

print('axes/rank ->', a.ndim)
print('shape ->', a.shape)
print('size ->', a.size)

# Reshaping arrays np.reshape/.reshape
a = np.arange(12)
a = a.reshape(3, 4)
print(a, '\n', a.shape)

b = a.reshape(-1)
print(b)
b = a.reshape(-1,1)
print(b)
b = a.reshape(3,2,-1)
print(b)
c = b.reshape(3,-1)
print(c)

# Return 1D-array -> .ravel
d = c.ravel()
print(d)

# Flatten -> like ravel but returns a copy , modification does not carry across flattend arrays
e = c.flatten()
print(e)

# Transposition -> Switch rows and columns with .T/.transpose()
a = np.arange(6).reshape(2,3)
print(a)
b = a.T
c = a.transpose()
print(b)
print(c)

