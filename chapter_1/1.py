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


print("_____________1.1.5______________________")
# create a random number generator
rng = np.random.default_rng()
# Generate random integers from 0 to 9
arr = rng.integers(low=0, high=10, size=(2, 4))
print(arr)


print("_____________1.1.6______________________")
# this method creates an array of random floats between 0 and 1
# int he shape of 2 rows and 4 columns
# create random generator
rng = np.random.default_rng(seed = 24)
# Generatre random floats between 0 and 1
arr = rng.random((2, 4))
print(arr)


print("_____________1.2______________________")
print("_____________1.2.1____________________")
# accessing array elements
# access a range of elements using a colon (a slice)
names = [["Jon", "Mary", "Paul"], ["Peter", "Ben", "Saul"]]
arr = np.array(names)
print(arr)

# lets say we want to slice out the names mary and pual here is how to do that
# they are the first row: 0
# in the first row they are the elements indexes 1 and 2
select_mary_paul = arr[0,1:]
print(select_mary_paul)
