with source as (
    select * from {{ ref('stg_excel__sales') }}
)

select
    store_id,
    store_location
from source
qualify
    row_number() over (partition by store_id order by transaction_dt desc nulls last)
    = 1
