import numpy as np

"""
NumPy program to create a 10x10 matrix,
in which the elements on the borders will be equal to 1, and inside 0
"""

if __name__ == '__main__':
    # define 10*10 matrix of zeroes
    matrix = np.zeros ((10, 10), dtype=int)
    # fill border with 1's.
    matrix[:, [0, -1]] = matrix[[0, -1]] = 1
    print(matrix)
