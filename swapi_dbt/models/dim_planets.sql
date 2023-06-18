{{ config(materialized='table') }}

with planets as (
  select planet_id, name from {{source('postgres', 'stg_planets')}}
)

select *
from planets
