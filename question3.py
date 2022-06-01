import numpy as np


def get_row_and_col(matrix: np.ndarray) -> tuple[int, int]:
    """
    function that return a set of 2 values (row,col) that represents the count
    of rows and cols in the given matrix.
    :param matrix: the given matrix
    :return: set of 2 values (row,col)
    """
    return matrix.shape


if __name__ == '__main__':
    matrix = np.arange(10,22).reshape((3, 4))
    print(get_row_and_col(matrix))
