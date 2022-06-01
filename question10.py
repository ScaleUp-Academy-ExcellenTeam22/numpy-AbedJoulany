import numpy as np

"""
Write a NumPy program to sort an along the first, last axis of an array
"""

nums = np.array([[4, 6],[2, 1]])
print("Original array: \n",nums)
x = np.sort(nums, axis=0)
print("Sort along the first axis: \n",x)
y = np.sort(x, axis=1)
print("Sort along the last axis: \n", y)
