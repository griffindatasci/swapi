{{ config(materialized='table') }}

with people as (
--  select 1 as id
  select people_id, name, height from {{source('postgres', 'stg_people')}}
)

select *
from people
