# Import libraries

import mysql.connector
import sys
import csv
from datetime import datetime
import re

try:
    # set the user and password
    # connect to mysql connector
    conn = mysql.connector.connect(
        user="general",
        password="Zikorachukwuzoey2020!",
        host="127.0.0.1",    
        port=3306             
    )

    # create and get the cursor
    cur = conn.cursor()

    cur.execute("DROP DATABASE IF EXISTS `pollution-db2`")
    cur.execute("CREATE DATABASE `pollution-db2`")

    # empty list to hold records
    records = [];

    # read in the csv file as a list one at a time
    with open('clean.csv','r') as csvfile: 
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
    
        for row in reader:
            records.append(row)
        
    # records[] is now a list of lists
    
    # create a database handle
    cur.execute("USE `pollution-db2`")
    
    # create required tables by defining the SQL for the tables
    my_stations_sql = """CREATE TABLE `stations`
                (`stationid` INT(10) NOT NULL,
                `location` VARCHAR(50) NOT NULL,
                `geo_point_2d` VARCHAR(50) NOT NULL,
                PRIMARY KEY(`stationid`));"""
    
    my_readings_sql = """CREATE TABLE `readings`
                (`readingsid` INT(10) NOT NULL AUTO_INCREMENT,
                `date Time` DATETIME NOT NULL,
                `NOx` FLOAT,
                `NO2` FLOAT,
                `NO` FLOAT,
                `PM10` FLOAT,
                `NVPM10` FLOAT,
                `VPM10` FLOAT,
                `NVPM2.5` FLOAT,
                `PM2.5` FLOAT,
                `VPM2.5` FLOAT,
                `CO` FLOAT,
                `O3` FLOAT,
                `SO2` FLOAT,
                `Temperature` REAL,
                `RH` INT,
                `Air Pressure` INT,
                `DateStart` DATETIME,
                `DateEnd` DATETIME,
                `Current` TEXT(5),
                `Instrument Type` VARCHAR(35),
                `stationid-fk` INT,
                PRIMARY KEY (`readingsid`));"""
            
    my_schema_sql = """CREATE TABLE `schema`
            (`measure` VARCHAR(32) NOT NULL,
            `description` VARCHAR(65),
            `unit` VARCHAR(30),
            PRIMARY KEY(`measure`));"""
            
            
    cur.execute(my_stations_sql)
    cur.execute(my_readings_sql)
    cur.execute(my_schema_sql)
    
    # add the relationships
    cur.execute("ALTER TABLE readings ADD FOREIGN KEY (`stationid-fk`) REFERENCES stations(stationid);")
   
    for row in records:
                
        #set autocommit flag to false
        conn.autocommit = False 
        
        #insert stations 
        my_stations_sql="""INSERT IGNORE INTO stations values(%s, %s, %s)"""
        svalues=(row[4], row[17], row[18])

        cur.execute(my_stations_sql, svalues)
        
#         # get stations id using SQL
        cur.execute("SELECT * FROM stations WHERE stationid = %s", (row[4],))
        
#         # set sid to query result
        sid = cur.fetchone()[0]
        
#         #insert readings
        my_readings_sql =  """INSERT IGNORE INTO `readings` values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        rvalues = ("", row[0], row[1], row[2], row[3], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], 
        row[19], row[20], row[21], row[22], sid)

        
        cur.execute(my_readings_sql, rvalues)
        
#     #insert schema
    my_schema_sql = """INSERT IGNORE INTO `schema` values(%s, %s, %s)"""
    sch_values = [("Date Time", "Date and time of measurement", "datetime"), ("NOx","Concentration of oxides of nitrogen", "μg/m3"), 
        ("NO2", "Concentration of nitrogen dioxide", "μg/m3"), ("NO", "Concentration of nitric oxide", "μg/m3"), ("SiteID",  "Site ID for the station","integer"),
        ("PM10", "Concentration of particulate matter <10 micron diameter", "μg/m3"), ("NVPM10", "Concentration of non - volatile particulate matter <10 micron diameter", "μg/m3"),
        ("VPM10", "Concentration of volatile particulate matter <10 micron diameter", "μg/m3"), ("NVPM2.5", "Concentration of non volatile particulate matter <2.5 micron diameter", "μg/m3"),
        ("PM2.5", "Concentration of particulate matter <2.5 micron diameter", "μg/m3"), ("VPM2.5", "Concentration of volatile particulate matter <2.5 micron diameter", "μg/m3"),
        ("CO", "Concentration of carbon monoxide", "mg/m3"), ("O3", "Concentration of ozone", "μg/m3"), ("SO2", "Concentration of sulphur dioxide", "μg/m3"),
        ("Temperature", "Air temperature", "°C"), ("RH", "Relative Humidity", "%"), ("Air Pressure", "Air Pressure", "mbar"), ("Location", "Text description of location", "text"),
        ("geo_point_2d", "Latitude and longitude", "geo point"), ("DateStart", "The date monitoring started", "datetime"), ("DateEnd", "The date monitoring ended", "datetime"),
        ("Current", "Is the monitor currently operating", "text"), ("Instrument Type", "Classification of the instrument", "text")]

    cur.executemany(my_schema_sql, sch_values) 


    conn.commit()
    conn.close()

# catch and report on any error
except BaseException as err:
    print(f"An error occured: {err}")
    sys.exit(1)