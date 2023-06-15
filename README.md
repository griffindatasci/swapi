# SWAPI > PostgreSQL Database

Aims: 
- Scrape data from the [Star Wars API (SWAPI)](https://swapi.dev/); datasets include films, planets, people (characters), starships, species, vehicles
- Use DBT to transform data
- Host database in PostgreSQL

Process:
- Install PostgreSQL
- Create a github repo at github.com
- Clone the repo to the local machine:
    1. Open the command prompt and navigate to a suitable host directory
    1. Execute `git clone <repo-name>`
    1. Close command prompt
    - Note: push material back to the git repo with `git add .`, `git commit -m "<message>"` and `git push origin`
- Install DBT on local machine:
    1. Open command prompt
    1. Execute `pip install dbt-postgres`
    1. Close command prompt
- Initialise the DBT project:
    1. Open command prompt and navigate to the github repo
    1. Execute `dbt init <database-name>`
    1. Close command prompt
- Update the profiles.yml file:
    1. This will be in the *Users/<pc-username>/.dbi* directory
    1. Add details for the dev section including port (5432), host (localhost), username and password for PostgreSQL
- Check setup:
    1. Open command prompt, navigate to the database directory (made at init, within the github repo)
    1. Execute `dbt debug`
    1. Execute `dbt run`
    1. Execute `dbt test` - note a fail may occur that requires uncommenting in *models/my_first_dbt_model.sql*; if so, edit, save then run and test again
- Create the PostgreSQL database:
    1. For now, ust go here: https://www.microfocus.com/documentation/idol/IDOL_12_0/MediaServer/Guides/html/English/Content/Getting_Started/Configure/_TRN_Set_up_PostgreSQL.htm
- Create tables in pgAdmin4
- Write and execute Python scripts to scrape data and transfer it to swapi_database

### TODO:

- Figure out how to get DBT involved in scrape/transform; suspect DBT will incorporate the work I am currently performing manually with python script execution (main.py and api_wan_kanapi.py)
- Design and implement schema (possible idea: dim_people, dim_films, dim_planets, fct_appearance (each observation is a character appearance per film, allowing summaries of e.g. which homeplanet was most represented in each film? which film had the greatest average character height? etc.) but not sure if this is a valid/legitimate way to use star-schema)



