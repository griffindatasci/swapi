{{ config(materialized='table') }}

with people as (
  select 1 as id
)

select *
from people
