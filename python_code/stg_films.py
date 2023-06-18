from api_wan_kenapi import api_wan
import psycopg2
from hidden import postgres_pwd
from variables import database_name, database_user, database_host, database_port


# Scrape data
films = api_wan("films")


# Create the table in PostgreSQL
command = """
CREATE TABLE IF NOT EXISTS "stg_films" (
    "film_id"	SERIAL PRIMARY KEY,
    "title"	CHAR(200),
    "episode_id"	CHAR(200),
    "opening_crawl"	CHAR(2000),
    "director"	CHAR(200),
    "producer"	CHAR(200),
    "release_date"	CHAR(200),
    "url"	CHAR(200),
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
command = """INSERT INTO stg_films (title, episode_id, opening_crawl, director, producer, release_date, url, created, edited) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);"""

with psycopg2.connect(database=database_name, 
                    user=database_user, 
                    password=postgres_pwd, 
                    host=database_host, 
                    port=database_port) as conn:
    cursor = conn.cursor()
    for film in films:
        cursor.execute(command, tuple([film["title"], 
                                       film["episode_id"], 
                                       film["opening_crawl"], 
                                       film["director"], 
                                       film["producer"], 
                                       film["release_date"], 
                                       film["url"], 
                                       film["created"], 
                                       film["edited"]]))
    conn.commit()
