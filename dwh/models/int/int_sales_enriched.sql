with source as (
    select * from {{ ref('stg_excel__sales') }}
),

enriched as (
    select
        transaction_id,
        store_id,
        product_id,
        store_location,
        product_category,
        product_type,
        product_detail,
        transaction_qty,
        unit_price,
        date_trunc('day', cast(transaction_dt as datetime)) as transaction_dt,
        date_trunc(
            'hour',
            cast((cast(transaction_dt as date) || ' ' || transaction_ts) as timestamp)
        ) as transaction_ts,
        round(transaction_qty * unit_price, 2) as order_revenue
    from source
),

final as (
    select
        transaction_id,
        store_id,
        product_id,
        store_location,
        product_category,
        product_type,
        product_detail,
        transaction_dt,
        transaction_qty,
        unit_price,
        order_revenue,
        strftime(transaction_ts, '%T') as transaction_ts,
        case
            when
                extract('hour' from transaction_ts) >= 6
                and extract('hour' from transaction_ts) < 12 then 'Morning'
            when
                extract('hour' from transaction_ts) >= 12
                and extract('hour' from transaction_ts) < 18 then 'Afternoon'
            when
                extract('hour' from transaction_ts) >= 18 then 'Night'
        end as work_shift
    from enriched
)

select * from final
