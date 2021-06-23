# We import a math library
import math

# Taking the input from user
fnumber = int(input("Enter the Number\n"))

# Use a math method called sqrt() which gets the square root of a number
p_root = math.sqrt(fnumber)

# Check if the root root can give the exact number as the input one
# This is when we square it after adding the 0.5 error
if int(p_root + 0.5) ** 2 == fnumber:
    print(fnumber, "it's a perfect square good guess")
else:
    print(fnumber, "Not a perfect square try better next time")