{{ config(materialized='table') }}

with appearances as (
  select * from {{source('postgres', 'fct_appearances')}}
)

select film_id, count(distinct(planet)) as n_planets from appearances group by film_id