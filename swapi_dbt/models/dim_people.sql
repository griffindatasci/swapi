{{ config(materialized='table') }}

with people as (
--  select 1 as id
    select people_id from {{ref('public.stg_people')}}
)

select *
from people
