CREATE TABLE flights_original (
                    callsign VARCHAR(255), 
                    flight_number INT, 
                    icao24 VARCHAR(255), 
                    registration VARCHAR(255), 
                    typecode VARCHAR(255),
                    origin VARCHAR(255), 
                    destination VARCHAR(255),  
                    first_time VARCHAR(255), 
                    last_time VARCHAR(255), 
                    flight_date DATE, 
                    latitude_1 VARCHAR(255), 
                    longitude_1 VARCHAR(255), 
                    altitude_1 VARCHAR(255), 
                    latitude_2 VARCHAR(255), 
                    longitude_2 VARCHAR(255), 
                    altitude_2 VARCHAR(255)
);

CREATE TABLE flights (
                    callsign VARCHAR(255),
                    origin VARCHAR(255),
                    destination VARCHAR(255)
);

CREATE TABLE airport_coordinates (
                    airport VARCHAR(255),
                    latitude VARCHAR(255),
                    longitude VARCHAR(255)
);

				