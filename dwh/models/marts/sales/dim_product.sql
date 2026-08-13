with source as (
    select * from {{ ref('stg_excel__sales') }}
)

select
    product_id,
    product_category,
    product_type,
    product_detail
from source
qualify
    row_number() over (partition by product_id order by transaction_dt desc nulls last)
    = 1
