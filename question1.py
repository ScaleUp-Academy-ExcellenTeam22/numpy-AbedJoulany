import numpy as np


if __name__ == '__main__':
    arr = np.arange(0, 21)
    print("vector before signing: ", arr)
    arr[9:16] *= -1
    print("vector after signing: ", arr)
