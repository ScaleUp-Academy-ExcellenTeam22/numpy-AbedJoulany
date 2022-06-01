import numpy as np
"""
Write a NumPy program to create a three-dimension array with shape (300,400,5) and set to a variable. Fill the array elements with values using unsigned integer (0 to 255)
"""
print(np.random.randint(low=0, high=256, size=(300, 400, 5), dtype=np.uint8))