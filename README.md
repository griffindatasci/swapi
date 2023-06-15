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
- Install DBT on local machine:
    1. Open command prompt
    1. Execute `pip install dbt-postgres`
    1. Close command prompt
- Initialise the PostgreSQL database:
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
