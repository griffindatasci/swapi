# SWAPI > PostgreSQL Database

### UPDATE (2023/06/18):
- Now working fully; takes raw data from API (by running python scripts), creates staging tables in python, and dbt creates dimension and fact tables. I added a summary of planets per film as a test that this works as expected to give "business" insight...

### Aims: 
- Scrape data from the [Star Wars API (SWAPI)](https://swapi.dev/); datasets include films, planets, people (characters), starships, species, vehicles
- Use DBT to transform data
- Host database in PostgreSQL
- (extra) Added summary of number of home planets (of characters featured in each film) per film

### My Process to make this (so far):
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
- Write and execute Python scripts to scrape data and transfer it to swapi_database
- Add .sql models
- Add sources.yml
- Run `dbt run`

