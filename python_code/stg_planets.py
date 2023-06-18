from api_wan_kenapi import api_wan
import psycopg2
from hidden import postgres_pwd
from variables import database_name, database_user, database_host, database_port


# Scrape data
planets = api_wan("planets")


# Create the table in PostgreSQL
command = """
CREATE TABLE IF NOT EXISTS "stg_planets" (
    "planet_id"	CHAR(200) PRIMARY KEY,
    "name"	CHAR(200),
    "diameter"	CHAR(200),
    "rotation_period"	CHAR(200),
    "orbital_period"	CHAR(200),
    "gravity"	CHAR(200),
    "population"	CHAR(200),
    "climate"	CHAR(200),
    "terrain"	CHAR(200),
    "surface_water"	CHAR(200),
    "created"	CHAR(200),
    "edited"	CHAR(200)
);
"""

with psycopg2.connect(database=database_name, 
                    user=database_user, 
                    password=postgres_pwd, 
                    host=database_host, 
                    port=database_port) as conn:
    cursor = conn.cursor()
    cursor.execute(command)
    conn.commit()



# Send data to the Postgresql database: swapi. 
command = """INSERT INTO stg_planets (planet_id, name, diameter, rotation_period, orbital_period, gravity, population, climate, terrain, surface_water, created, edited) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

with psycopg2.connect(database=database_name, 
                    user=database_user, 
                    password=postgres_pwd, 
                    host=database_host, 
                    port=database_port) as conn:
    cursor = conn.cursor()
    for planet in planets:
        cursor.execute(command, tuple([planet["url"], 
                                       planet["name"], 
                                       planet["diameter"], 
                                       planet["rotation_period"], 
                                       planet["orbital_period"], 
                                       planet["gravity"], 
                                       planet["population"], 
                                       planet["climate"], 
                                       planet["terrain"], 
                                       planet["surface_water"], 
                                       planet["created"], 
                                       planet["edited"]]))

    conn.commit()
