from api_wan_kenapi import api_wan
import psycopg2

pwd = input("Enter password for postgresql: ")
people = api_wan("people")


# This is to reduce the number of variables
# - reduces workload on setup in Postgresql(?)
# - removes the headache of how to handle lists (e.g. people.films) 
#      which is not needed just yet...
people_focal = [{#"people_id":person["url"].split("/")[-2],
                 "name":person["name"], 
                 "homeworld":person["homeworld"],
                 "gender":person["gender"], 
                 "height":person["height"], 
                 "mass":person["mass"] } 
                 for person in people]


# Run this if need to make the table
if False:
    command = """
    CREATE TABLE "people" (
        "people_id"	SERIAL PRIMARY KEY,
        "name"	CHAR(200),
        "homeworld"	CHAR(200),
        "gender"	CHAR(200),
        "height"	CHAR(200),
        "mass"	CHAR(200)
    );
    """
    with psycopg2.connect(database="swapi_database", 
                        user="postgres", 
                        password=pwd, 
                        host="localhost", 
                        port=5432) as conn:
        cursor = conn.cursor()
        cursor.execute(command)
        conn.commit()


# Send data to the Postgresql database, swapi. 
# - Database and table have already been create in pgAdmin4
command = """INSERT INTO people (name, homeworld, gender, height, mass) VALUES (%s, %s, %s, %s, %s);"""

with psycopg2.connect(database="swapi_database", 
                      user="postgres", 
                      password=pwd, 
                      host="localhost", 
                      port=5432) as conn:
    cursor = conn.cursor()
    for person in people_focal:
        cursor.execute(command, tuple(person.values()))
    conn.commit()
