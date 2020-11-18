import csv
from os import listdir
from os.path import isfile, join
import gzip
import json
import mysql.connector


# Cursor

cnx = mysql.connector.connect(user='root', password='pass',
                                host='52.14.118.167',
                                database='flights_db',
                                auth_plugin='mysql_native_password')

cursor = cnx.cursor()


path = './temp_dir'
files = [f for f in listdir(path) if isfile(join(path, f))]

file_ex = files[0]

with gzip.open(f'{path}/{file_ex}', 'rt', newline='\n') as file:
    file = csv.reader(file, delimiter=',')

    flight_data = ((row[0], row[5], row[6]) for row in file)
    flight_data = list(filter(lambda x: x[0] != '' and x[1] != '', flight_data))


# Add data into flights

add_flight = ('INSERT INTO flights '
               "(callsing, origin, destination)"
               "VALUES (%(flight_number)s, %(origin)s, %(destination)s)")


cursor.execute(add_flight, flight_data)
emp_no = cursor.lastrowid

with open('./airport_coordinates.json', 'r') as fh:
    result_dict = json.load(fh)

