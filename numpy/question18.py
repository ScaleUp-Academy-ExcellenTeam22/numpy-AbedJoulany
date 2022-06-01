import numpy as np

"""
Write a NumPy program to count the number of days of specific month.  
"""

print("Number of days, February, 2016: ")
print(np.datetime64('2016-03-01') - np.datetime64('2016-02-01'))
print("Number of days, February, 2017: ")
print(np.datetime64('2017-03-01') - np.datetime64('2017-02-01'))
print("Number of days, February, 2018: ")
print(np.datetime64('2018-03-01') - np.datetime64('2018-02-01'))