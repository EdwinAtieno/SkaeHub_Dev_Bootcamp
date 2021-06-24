#Import the numpy library.
import numpy as np

#find today's date using the datetime64() function.
today = np.datetime64('today', 'D')
print("Today: ",today)

#find yesterday's date by subtracting the output of timedelta64() function of one day from the output of datetime64() function of today.
# the D represent one day
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yestraday: ",yesterday)

#Find tomorrows's date by adding the output of timedelta64() function of one day to the output of datetime64() function of today.
tomorrow = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: ",tomorrow)