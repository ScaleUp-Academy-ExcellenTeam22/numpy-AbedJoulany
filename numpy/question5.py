import numpy as np
"""
Write a NumPy program to add a vector to each row of a given matrix
"""

if __name__ == '__main__':
    # define 10*10 matrix of zeroes
    matrix = np.array ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    vector = np.array ([1, 2, 3])
    print("vector before adding the vector: \n", matrix)
    print("vector: \n", vector)
    matrix[0:, 0:] += vector
    print("vector after adding the vector: \n", matrix)
