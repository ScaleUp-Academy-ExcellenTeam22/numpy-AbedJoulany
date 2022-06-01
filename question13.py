import numpy as np
"""
Write a NumPy program to convert (in sequence depth wise (along third axis)) two 1-D arrays into a 2-D array
"""
print("Sample array: (10,20,30), (40,50,60)")
print("output:\n",np.dstack((np.array([[10],[20],[30]]), np.array([[40],[50],[60]]))))