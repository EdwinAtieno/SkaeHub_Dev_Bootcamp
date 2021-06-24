# import library
import numpy as np

# create an list
x = []

# ask the size of array needed
a = int(input("Size of array:\n"))

# ask user to input the element they want to put
for i in range(a):
    #add data to the list
    x.append(float(input("Element:\n")))

# change the list to a numpy array
x = np.array(x)
print(x)

# check the length of array
if len(x) >5:

    # get the size of the array
    print("Size of the array: ",
          x.size)

    # get the memory size of one array element
    print("Memory size of one array element in bytes: ",
          x.itemsize)

    # memory size of numpy array in bytes(all elements)
    print("Memory size of numpy array in bytes:",
          x.size * x.itemsize)