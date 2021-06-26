# Create a function to select maximum and minimum
def max_min_tuples(numbers):
    # Use max method to get the maximum and use lambda function
    # to get value in the indicated index
    return_max1 = max(numbers, key=lambda item: item[0])[0]
    return_min1 = min(numbers, key=lambda item: item[0])[0]

    # Use max method to get the minimum and use lambda function
    # to get value in the indicated index
    return_max2 = max(numbers, key=lambda item: item[1])[1]
    return_min2 = min(numbers, key=lambda item: item[1])[1]
    return [return_max1, return_min1, return_max2, return_min2]

# input you values(tuples) in a list
students = [(22, 62), (32, 68), (1, 72), (48, 70), (9, 74), (10, 65)]
print("Original list with tuples:")
print(students)
print("\nMaximum and minimum values of the said list of tuples:")

# Call the function then pass the list in the function
print(max_min_tuples(students))