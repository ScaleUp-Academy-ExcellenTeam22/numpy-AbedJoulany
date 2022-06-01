import numpy as np

"""
Write a NumPy program to compute the median of flattened given array.  
Note: First array elements raised to powers from second array
"""

arr = np.arange(12).reshape((2, 6))
print("Original array:\n",arr)
print("\nMedian of said array:\n", np.median(arr))
