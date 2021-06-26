# import Nominatim
from geopy.geocoders import Nominatim

# set user_agent- is an http request header that is sent with each request.
geolocator = Nominatim(user_agent="geoapiExercises")

# Prompt user to enter the City he or she wants
state1 = input("enter name of state/city\n")
print("State Name:",state1)

# use geolocator() and geocode() function and method to locate the country address using City name
location = geolocator.geocode(state1)
print("State Name/Country Name: ")

# Use address method to map the name of country
print(location.address)
