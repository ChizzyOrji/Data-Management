# Import libraries

import csv

# open and read in the csv file

with open ("bristol-air-quality-data.csv", "r", newline="") as file:
    reader = csv.reader(file, delimiter=';')

    # open and write into new csv file
    with open("./cropped.csv", "w", newline="") as new_file:
       writer = csv.writer(new_file, delimiter=';')

       for row in reader:
           if row[0] >= '2010-01-01T00:00:00+00:00':
            writer.writerow(row)

            