# import Nominatim
from geopy.geocoders import Nominatim
# set user_agent- is an http request header that is sent with each request.
geolocator = Nominatim(user_agent="geoapiExercises")

#prompt user to enter the zipcode of the place
zipc = input("Enter a zip code ")
print("\nTOWN NAME", zipc)

# use geolocator() and geocode() function and method to locate the country address using City name
location = geolocator.geocode(zipc)
print("Details of the said pincode:")

#Use address method to map the name of country
print(location.address)

print("Else if you want to use the town")

#prompt user to enter the zipcode of the place
town = input("\nEnter a town name ")
print("\nTOWN NAME", town)

# use geolocator() and geocode() function and method to locate the country address using City name
location = geolocator.geocode(town)
print("Details of the said pincode:")

#Use address method to map the name of country
print(location.address)



