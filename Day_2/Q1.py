# Function to check if x is power of 4
def PowerFour(x):
    # this checks if x is equal to zero which is automatically not a power
    if (x == 0):
        return False
    #it iterates until the remainder is 0
    while (x != 1):
        if (x % 4 != 0):
            # then prints False if it's not equals to 0
            return False
        # after check, the value of n changes, which is then
        # checked until value = 0
        x = x // 4

    return True


# Driver code
test_no = int(input("Enter a number "))
# Print the output of the value inputed
if (PowerFour(test_no)):
    print(test_no, 'is a power of 4')
else:
    print(test_no, 'is not a power of 4')