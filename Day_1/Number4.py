import csv

# Open the file in read mode
with open('03-17-2020.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)  # use dictreader method to reade the file in dictionary

    for row in csv_reader:  # Iterate through the loop to read line by line
        print(row)