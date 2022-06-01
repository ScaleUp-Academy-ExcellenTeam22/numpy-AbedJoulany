import numpy as np

"""
Write a NumPy program to replace all numbers in a given array which is equal,
less and greater to a given number
"""
vector = np.arange(1,17).reshape(4,4)
print("array:\n", vector)
num = 8
replacement = 0
print(f"\nReplace elements that equals to {num} with {replacement}")
print(np.where(vector == num, replacement, vector))
print(f"\nReplace elements that greater than {num} with {replacement}")
print(np.where(vector < num, replacement, vector))
print(f"\nReplace elements that less than {num} with {replacement}")
print(np.where(vector > num, replacement, vector))