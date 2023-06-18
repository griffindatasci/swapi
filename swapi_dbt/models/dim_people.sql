{{ config(materialized='table') }}

with people as (
  select people_id, name, height, homeworld from {{source('postgres', 'stg_people')}}
)

select *
from people
