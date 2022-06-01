import numpy as np

"""
Write a NumPy program to combine a one and a two dimensional array together and display their elements
"""
one_d = np.arange(4)
print("One dimensional array:\n", one_d)
two_d = np.arange(8).reshape(2, 4)
print("Two dimensional array:\n", two_d)
for a, b in np.nditer([one_d, two_d]):
    print("%d:%d" % (a,b),)