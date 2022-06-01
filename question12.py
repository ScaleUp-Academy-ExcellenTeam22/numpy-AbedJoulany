import numpy as np
"""
Write a NumPy program to remove single-dimensional entries from a specified shape
"""
print("specified shape: ", (3, 1, 4))
print(np.squeeze(np.zeros((3, 1, 4))).shape)