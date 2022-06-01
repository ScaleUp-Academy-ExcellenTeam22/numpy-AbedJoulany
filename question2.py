import numpy as np


def create_vector(minimum: int, maximum: int, length: int) -> np.ndarray:
    """
    function to create a vector in range with evenly distributed values
    :param minimum: minimum in range
    :param maximum: maximum in range
    :param length: length of the vector
    :return: vector with evenly distributed values in range
    """
    return np.linspace(minimum, maximum, length)


if __name__ == '__main__':
    print (create_vector (5, 50, 10))
