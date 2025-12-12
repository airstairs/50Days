import numpy as np

print("_____________1.1.1______________________")
lst = [1, 2, 3, 4, 5, 6]
# creating an array from list
arr = np.array(lst)
print(arr)
print()
# creating an array of floats from list
arr = np.array(lst, dtype=float)
print(arr)
print()

# create multi dimensional array from nested list
names = [["Jon", "Mary", "Paul"], ["Peter", "Ben", "Saul"]]
arr = np.array(names)
print(arr)
print()
print("array dimensions")
print(f"length: {arr.shape}")
print(f"nDimensions: {arr.ndim}")


print("_____________1.1.2______________________")
# this function creates an array with regularly spaced values
arr = np.arange(0, 50, 5)
print(arr)


print("_____________1.1.3______________________")
# this function creates an array with all elements set to zero
arr = np.zeros((2, 3), dtype=float)
print(arr)


print("_____________1.1.4______________________")
# this creates an array with all elements set to 1
arr = np.ones((2, 3), dtype = float)
print(arr)
