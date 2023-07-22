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
print(np.linspace(1,13, num=5))

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
print(np.random.randint(10,size=(2,3)))
print(np.random.randint(10,100,size=4))

# .permutation = random permutation of numbers.
print(np.random.permutation(10))
print(np.random.permutation(["one", "two", "three", "four", "five"]))

# np.ones, np.zeros,np.full
print(np.ones(4))
print(np.ones((2,4)))
print(np.ones(4,dtype=bool))

print(np.zeros(4))
print(np.zeros((2,4)))
print(np.zeros(4,dtype=bool))

print(np.full(4,'rabbit'))
