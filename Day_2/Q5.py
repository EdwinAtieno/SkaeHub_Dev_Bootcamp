#import library
import requests

# Write the URL you want
url= "https://www.freecodecamp.org/news/how-to-use-chakra-ui-with-next-js-and-react/"


# Specify time in seconds required to retrive the url
try:
    report = requests.get(url, timeout=6)

# when timeout is exceed
except requests.exceptions.Timeout as error:
    print("Server is slow ", error)