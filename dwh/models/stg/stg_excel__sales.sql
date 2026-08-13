with source as (
    select * from {{ source('db', 'sales') }}
)

select
    transaction_id,
    store_id,
    product_id,
    store_location,
    product_category,
    product_type,
    product_detail,
    transaction_date as transaction_dt,
    transaction_time as transaction_ts,
    transaction_qty,
    unit_price
from source
