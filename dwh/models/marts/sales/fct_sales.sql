with source as (
    select * from {{ref('int_sales_enriched')}}
)

select
    transaction_id,
    store_id,
    product_id,
    work_shift,
    transaction_dt,
    transaction_ts,
    transaction_qty,
    unit_price,
    order_revenue
from source