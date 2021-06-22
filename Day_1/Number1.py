# Create a function which checks on the conditions
def Ifleap(year):
    # set the leap variable as False
    leap = False
    # Check if the year input meets the condition
    if year % 400 == 0:
        # set leap true if it meets the condition
        leap = True
    elif year % 100 == 0:
        # else set leap False if it does not meet the condition
        leap = False
    elif year % 4 == 0:
        leap = True
    return leap

# Prompt the user to enter a rando year
year = Ifleap(int(input("Enter any year:  ")))

#print the answer by passing the input through the function
print ((year))

print("\nWelcome ")