{{ config(materialized='table') }}

with people as (
--  select 1 as id
    select people_id UNIQUE NOT NULL from {{ ref('stg_people')}}
)

select *
from people
