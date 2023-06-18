{{ config(materialized='table') }}

with people as (
--  select 1 as id
  select * from {{source('swapi', 'stg_people')}}
)

select *
from people
