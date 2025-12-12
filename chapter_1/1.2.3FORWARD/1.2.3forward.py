import numpy as np

print("_____________1.2.3______________________")
# Boolean Indexing
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# create a boolean mask based on the condition
filter_array = arr % 2 != 0
print(arr)
print(filter_array)
# select the elements from the original array based on the filter
selected = arr[filter_array]
print(selected)
