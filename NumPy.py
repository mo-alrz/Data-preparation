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

# .random = Return random floats in the half-open interval [0.0, 1.0). Alias for random_sample to ease forward-porting
# to the new random API.
rand_arr = np.random.random()
print(rand_arr)
rand_arr = np.random.random([5,3])
print(rand_arr)

# .permutation = random permutation of numbers.
print(np.random.permutation(10))
print(np.random.permutation(["one", "two", "three", "four", "five"]))

# .uniform = random float number wit a capability to select max and min
arr1 = np.random.uniform()
arr2 = np.random.uniform(size=5)
arr3 = np.random.uniform(low=3, high=5, size=5)
arr4 = np.random.uniform(low=3, high=5, size=(2, 3))

# print only n decimal places in python numpy array -> .set_printoptions()
rand_arr = np.random.random([5,3])
np.set_printoptions(precision=3)
print(rand_arr)

# np.ones, np.zeros,np.full
print(np.ones(4))
print(np.ones((2, 4)))
print(np.ones(4, dtype=bool))

print(np.zeros(4))
print(np.zeros((2, 4)))
print(np.zeros(4, dtype=bool))

print(np.full(4, 'rabbit'))

# .where()
arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
rint(out)

# Get all items between 5 and 10 from a
a = np.array([2, 6, 1, 9, 10, 3, 27])
# 1
index = np.where((a >= 5) & (a <= 10))
# 2
index = np.where(np.logical_and(a >= 5, a <= 10))
# 3
index = a[(a >= 5) & (a <= 10)]

# make a python function that handles scalars to work on numpy arrays
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])


def maxx(x, y):
    if x >= y:
        return x
    else:
        return y


pair_max = np.vectorize(maxx, otypes=[float])
print(pair_max(a, b))

# .repeat()
a = np.repeat(1, 10)
print(a)

# Swap two columns/rows
arr = np.arange(9).reshape(3, 3)

# rows 1 and 2:
b = arr[[1, 0, 2], :]

# columns 1 and 2:
b = arr[:, [1, 0, 2]]

# Reverse rows and columns
arr = np.arange(9).reshape(3, 3)

# rows
a = arr[::-1]

# columns
b = arr[:, ::-1]

# Create a 2D array containing random floats between 5 and 10
rand_int = np.random.randint(low=5, high=10, size=(5, 3))
rand_float = np.random.random((5, 3))
c = rand_int + rand_float
print(c)

rand_arr = np.random.uniform(5, 10, size=(5, 3))
print(rand_arr)

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
b = a.reshape(-1, 1)
print(b)
b = a.reshape(3, 2, -1)
print(b)
c = b.reshape(3, -1)
print(c)

# Return 1D-array -> .ravel
d = c.ravel()
print(d)

# Flatten -> like ravel but returns a copy , modification does not carry across flattend arrays
e = c.flatten()
print(e)

# Transposition -> Switch rows and columns with .T/.transpose()
a = np.arange(6).reshape(2, 3)
print(a)
b = a.T
c = a.transpose()
print(b)
print(c)

# Operations
# Addition :
print([1, 1, 1] + [1, 2, 3])
print(np.array([1, 1, 1]) + np.array([1, 2, 3]))

# To concatenate :
print(np.concatenate([np.array([1, 1, 1]), np.array([1, 2, 3])]))

# Appending an element to a numpy array doesn't update original array:
a = np.array([1, 2, 3])
np.append(a, 4)
print(a)

# Stack two array vertically and horizontally:
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

# Vertically ->
c = np.concatenate([a, b], axis=0)
d = np.vstack([a, b])
e = np.r_[a, b]
print(c)
print(d)
print(e)

# Horizontally ->
c = np.concatenate([a, b], axis=0)
d = np.hstack([a, b])
e = np.c_[a, b]
print(c)
print(d)
print(e)

# .tile()
a = np.array([1, 2, 3])
b = np.tile(a, 3)
print(b)

# Intersection
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
c = np.intersect1d(a, b)
print(c)

# How to remove from one array those items that exist in another
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
c = np.setdiff1d(a, b)
print(c)

# How to get the positions where elements of two arrays match?
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
c = np.where(a == b)
print(c)

# Addition and multiplication of an element to a NumPy is elementwise addition
a = np.array([1, 1, 1])
print(a + 3)
print(a.dot(a))

# Should be of same length else it will raise error
a = np.arange(12).reshape(3, 4)
b = np.array([10 ** i for i in range(4)])
print(a + b)

a = np.arange(12).reshape(4, 3)
b = np.array([10 ** i for i in range(4)]).reshape(-1, 1)
print(a + b)

# Logical operators
a = np.array([1, 0, 0]).astype('bool')
b = np.array([1, 1, 0]).astype('bool')
print(a)
print(b)

# NOT AND OR XOR (We cannot use 'not,and')
print(~ a)
print(a & b)
print(a | b)
print(a ^ b)

# == < > <= >=
a = np.arange(6).reshape(2, 3)
b = np.array([[0, 1, 4], [3, 3, 5]])
print(a == b)
print(a < b)
print(a > b)

# .all() -> Shows if all elements are the same
# .any() -> Shows if any elements are the same
print((a == b).all())
print((a == b).any())

# For element-wise comparisons the arrays should be of the same shape
# if possible, NumPy will try to force elements into a common type
a = np.ones(4).astype('bool')
b = np.ones(4).astype('float')
c = np.ones(4).astype('int')

print(a == b)
print(b == c)
print(a == c)

a = np.full(4, fill_value=2).astype("int")
b = np.ones(4).astype("float")
c = np.ones(4).astype("bool")

print("a == b:", a == b)
print("a == c:", a == c)
print("b == c:", b == c)

a = np.array(["True"] * 4, dtype="object")
b = np.array(["True"] * 4, dtype="<U4")
c = np.ones(4).astype("bool")

print(a == b)
print(a == c)
# print(b == c)

# Checking level-equality
a = np.arange(6).reshape(2, 3)
b = np.arange(8).reshape(2, 4)

print(np.array_equal(a, b))

# Aggregations
# .sum() .mean() .min() .max() .argmin() .argmax()

a = np.arange(10, 15)
print(a.sum())
print(a.min())
print(a.max())
print(a.mean())
print(a.argmin())
print(a.argmax())

# Boolean indexing
a = np.array([1, 2, 3])
b = np.array([True, True, False])

print(a[b])
print(a[a <= 2])

# Booleans must be in same shape with the array, the result will be 1D array
a = np.arange(6).reshape(2, 3)
b = np.array([[True, True, False],
              [True, True, False]])

print(a[a < 5])
print(a[b])

# Empty values
print(np.array([None, np.NAN]))

print(np.NaN < 3)
print(np.NaN >= 3)

a = np.array([1, np.NaN, 1, 3])
print(a[a < 2])
print(a[a >= 2])
print(a[~(a < 2)])
