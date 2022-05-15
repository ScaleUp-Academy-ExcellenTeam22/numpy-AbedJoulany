import numpy as np

"""
Write a NumPy program to multiply two given arrays of same size element-by-element.
"""

nums1 = np.array([1,2,3])
nums2 = np.array([5, 3, 4])
print("array1:\n",nums1)
print("array2:\n",nums2)
print("\narrays after multiplication:\n",np.multiply(nums1, nums2))