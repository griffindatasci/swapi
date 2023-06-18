{{ config(materialized='table') }}

with people as (
    select * from stg_people
)

select *
from people
