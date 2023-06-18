from api_wan_kenapi import api_wan
import psycopg2
from hidden import postgres_pwd
from variables import database_name, database_user, database_host, database_port


# Scrape data
people = api_wan("people")


# Create the table in PostgreSQL
command = """
CREATE TABLE IF NOT EXISTS "stg_people" (
    "people_id" CHAR(200),
    "name"	CHAR(200),
    "birth_year" CHAR(200),
    "eye_color" CHAR(200),
    "gender" CHAR(200),
    "hair_color" CHAR(200),
    "height" CHAR(200),
    "mass" CHAR(200),
    "skin_color" CHAR(200),
    "homeworld"	CHAR(200),
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
command = """INSERT INTO stg_people VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s);"""

with psycopg2.connect(database=database_name, 
                    user=database_user, 
                    password=postgres_pwd, 
                    host=database_host, 
                    port=database_port) as conn:
    cursor = conn.cursor()
    for person in people:
        cursor.execute(command, tuple([person["url"], 
                                       person["name"], 
                                       person["birth_year"], 
                                       person["eye_color"], 
                                       person["gender"], 
                                       person["hair_color"], 
                                       person["height"], 
                                       person["mass"], 
                                       person["skin_color"], 
                                       person["homeworld"], 
                                       person["created"], 
                                       person["edited"]]))
    conn.commit()
