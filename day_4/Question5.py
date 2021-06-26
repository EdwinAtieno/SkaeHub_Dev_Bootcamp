# import iterating tool to help iterating
import itertools as it

# Create a function
def cycle_data(iter):

    # call The Function takes only one argument as input it can be like list, String, tuple, etc- cycle()
    return it.cycle(iter)

# Following  loops will run for ever
# Iterate for List
result = cycle_data([21,56,60,12])
print("The said function print never-ending items:")

# use for loop to loop and print the result
for i in result:
    print(i)

# Iterate for String
result = cycle_data('Python itertools')
print("The said function print never-ending items:")
for i in result:
    print(i)

