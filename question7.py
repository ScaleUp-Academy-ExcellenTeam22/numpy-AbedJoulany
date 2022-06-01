import numpy as np

"""
Write a NumPy program to create a 4x4 array with random values,
now create a new array from the said array swapping first and last rows
"""
matrix = np.arange(16, dtype=int).reshape(4, 4)
print("before swapping: \n", matrix)
matrix = matrix[::-1]
print("after swapping: \n", matrix)