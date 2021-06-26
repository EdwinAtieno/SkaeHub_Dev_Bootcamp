# create a list containing dictionaries
phones = [{'make':'Nokia', 'model':216, 'color':'Brown'}, {'make':'Motorola', 'model':'2', 'color':'pink'}, {'make':'Huawei', 'model': 7, 'color':'Blue'}]
print("Original list of dictionaries :")

# Print to confirm
print(phones)
print("\nOriginal list of dictionaries :")

# Use the sorted() to sort the dictionary using any key of choice and use Lambada also
sorted=sorted(phones, key=lambda x: x['make'])
print(sorted)