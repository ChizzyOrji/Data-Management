# import libraries
import csv

# create a list for headers
header = ['Date Time', 'NOx', 'NO2', 'NO', 'SiteID', 'PM10', 'NVPM10', 'VPM10', 'NVPM2.5', 'PM2.5', 'VPM2.5', 'CO', 'O3', 'SO2', 'Temperature', 'RH', 'Air Pressure', 'Location', 
'geo_point_2d', 'DateStart', 'DateEnd', 'Current', 'Instrument Type']

#create a dictionary for the stations
location_dictionary = {'188':'AURN Bristol Centre',
'203':'Brislington Depot',
'206':'Rupert Street',
'209':'IKEA M32',
'213': 'Old Market',
'215':'Parson Street School',
'228':'Temple Meads Station',
'270':'Wells Road',
'271':'Trailer Portway P&R',
'375':'Newfoundland Road Police Station',
'395':"Shiner's Garage",
'452':'AURN St Pauls',
'447':'Bath Road',
'459':'Cheltenham Road \ Station Road',
'463':'Fishponds Road',
'481':'CREATE Centre Roof',
'500':'Temple Way',
'501':'Colston Avenue'}

# open and read csv file
with open("cropped.csv", "r", newline="\n") as file:
    reader = csv.reader(file, delimiter=';')

    # open and write into new file
    with open("./clean.csv", "w", newline="\n") as new_file:
        writer = csv.writer(new_file)
        
        # write the header
        writer.writerow(header)

        line_number = 1
        next(reader)

        for row in reader:
            site_id = row[4]
            if len(site_id) > 0 and (site_id in location_dictionary) and location_dictionary[site_id] == row[17]:

                # write the rows
                writer.writerow(row)
            else:
                if len(site_id) == 0:
                    print("site id in row: ",line_number, "is empty")
                elif site_id not in location_dictionary:
                    print("line: ",line_number, "with site_id: ", site_id, "does not match", row[17])
                elif location_dictionary[site_id] != row[17]:
                    print("line: ",line_number,"in", location_dictionary[site_id], " does not match ", row[17])
                    
            line_number += 1

