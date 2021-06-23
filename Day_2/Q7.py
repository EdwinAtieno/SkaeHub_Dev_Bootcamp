# import a library from python which will be able to get a page from browser
import requests

# Write the URL you want to get the data
url = 'https://jsonplaceholder.typicode.com/todos/1'

#Fetch the data from URL
response = requests.get(url)

# To print http response code
print(response.status_code)

# It place the content of the browser page into dictionary object
print(response.__dict__)