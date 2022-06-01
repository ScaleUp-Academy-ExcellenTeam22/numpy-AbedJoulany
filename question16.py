import numpy as np

"""
Write a NumPy program to sort the student id with increasing height of the students from given students id and height.
Print the integer indices that describes the sort order by multiple columns and the sorted data
"""
student_id = np.array([100, 200, 300, 400, 500, 600, 700])
student_height = np.array([78., 54., 94., 68., 42., 73., 55.])
indices = np.lexsort((student_id, student_height))
print("sorting by indices:\n", indices)
print("Sorted data:")
for n in indices:
  print(student_id[n], student_height[n])