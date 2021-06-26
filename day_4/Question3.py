# Import Nominatim
from geopy.geocoders import Nominatim

# set user_agent- is an http request header that is sent with each request.
geolocator = Nominatim(user_agent="geoapiExercises")

# Prompt user to input latitudes and longitude and separate them using space
lald = str(input("enter your Latitude and longitude separated by space\n"))

# print the altitude and longitude
print("Latitude and Longitude:",lald)

# use geolocator() and geocode() function and method to locate the address using the
# longitude and latitude
location = geolocator.geocode(lald)
print("Location address of the said Latitude and Longitude:")
print(location)
