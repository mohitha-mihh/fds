# Ex 1: Working with NumPy arrays - array operations, aggregation, boolean logic, broadcasting
import numpy as np

# Array creation
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.arange(1, 10).reshape(3, 3)
print("Array a:\n", a)
print("Shape:", a.shape, "| Dim:", a.ndim, "| Dtype:", a.dtype)

# Array operations
print("\nAddition:\n", a + b)
print("Multiplication (element-wise):\n", a * b)
print("Matrix product:\n", a @ b)
print("Transpose:\n", a.T)
print("Square root:\n", np.sqrt(a))

# Aggregation
print("\nSum:", a.sum(), "| Mean:", a.mean(), "| Std:", a.std())
print("Min:", a.min(), "| Max:", a.max())
print("Column sums:", a.sum(axis=0))
print("Row means:", a.mean(axis=1))
print("Argmax:", a.argmax(), "| Cumulative sum:", a.cumsum())

# Boolean logic
print("\na > 5:\n", a > 5)
print("Elements > 5:", a[a > 5])
print("Even numbers:", a[a % 2 == 0])
print("Between 3 and 7:", a[(a > 3) & (a < 7)])
print("Any > 8:", np.any(a > 8), "| All > 0:", np.all(a > 0))
print("Count of values > 4:", np.sum(a > 4))

# Broadcasting
row = np.array([10, 20, 30])
col = np.array([[1], [2], [3]])
print("\nMatrix + row (broadcast):\n", a + row)
print("Matrix * column (broadcast):\n", a * col)
print("Column + row -> 3x3:\n", col + row)
print("Mean-centered columns:\n", a - a.mean(axis=0))
