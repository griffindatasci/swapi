{{ config(materialized='table') }}

with appearances as (
  select * from {{source('postgres', 'stg_appearances')}}
),
people_planets as (
  select dim_people.people_id, dim_planets.name from dim_people left join dim_planets on dim_people.homeworld=dim_planets.planet_id
)

select appearances.*, people_planets.name as planet
from appearances left join people_planets on character_id=people_id

