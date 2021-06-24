# import numpy library
import numpy as np

# ask user to input date and a year in a given format
print("Enter the year and month to be counted and to which month, format(eg. 2021-06) :\n")

# prompt user to input month and year for the first to end
a= input("first month and year\n" ' ')
b= input("end month and year\n" ' ')

# use the busday_count() function to count the days and
# datetime64() function to accept the input as date
print(np.busday_count(np.datetime64(a), np.datetime64(b)))