from api_wan_kenapi import api_wan
import psycopg2
from hidden import postgres_pwd
from variables import database_name, database_user, database_host, database_port


# Scrape data
films = api_wan("films")


# Create the table in PostgreSQL
command = """
CREATE TABLE IF NOT EXISTS "stg_appearances" (
    "appearance_id"	SERIAL PRIMARY KEY,
    "film_id"	CHAR(200),
    "character_id"	CHAR(200)
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
command = """INSERT INTO stg_appearances (film_id, character_id) VALUES (%s, %s);"""

with psycopg2.connect(database=database_name, 
                    user=database_user, 
                    password=postgres_pwd, 
                    host=database_host, 
                    port=database_port) as conn:
    cursor = conn.cursor()
    for film in films:
        url = film["url"]
        for character in film["characters"]:
            cursor.execute(command, tuple([url, character]))
    conn.commit()

