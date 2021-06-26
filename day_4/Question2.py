# to load cities dataset
#to read more about geopy- https://geopy.readthedocs.io/en/stable/#module-geopy.distance
# import pandas to allow array
import pandas as pd

# to calculate distance on the surface
from geopy import distance

# load the dataframe with capitals
dataframe = pd.read_csv("concap.csv")

# rename so that the column names are shorter and comply with PEP-8
dataframe.rename(columns={"CountryName": "Country", "CapitalName": "capital", "CapitalLatitude": "lat", "CapitalLongitude": "lon", "CountryCode": "code", "ContinentName": "continent"}, inplace=True)
print(dataframe.sample(3))

# to start with let's filter only 2 capitals using the function isin(). Cairo and Nairobi.
tao = dataframe[dataframe["capital"].isin(["Cairo", "Nairobi"])].reset_index()
print(tao)

# Out put and calculate distance using distance() function
dist = distance.distance((tao.loc[0, "lat"], tao.loc[0, "lon"]), (tao.loc[1, "lat"], tao.loc[1, "lon"]))
print("distance in kilometer=", dist.km, "\ndistance in miles=", dist.miles)
