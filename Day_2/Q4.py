#import request library so to get a URL
import requests

#intiate the url
res = requests.get('https://www.freecodecamp.org/news/how-to-use-chakra-ui-with-next-js-and-react/')

# print the content of the response in Unicode
print("Response text of Freecode camp:")
print(res.text)

# print the content of the response in bytes.
print("\nContent of the said url:")
print(res.content)

# program or application to provide custom headers for the specific protocol
print("\nRaw data of the said url:")
r = requests.get('https://api.github.com/events', stream = True)
print(r.raw)

# The length of the raw information
print(r.raw.read(15))