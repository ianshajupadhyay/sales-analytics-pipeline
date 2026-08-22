with customer_records as (

    select
        customer_unique_id,
        customer_id,
        customer_city,
        customer_state,

        row_number() over (
            partition by customer_unique_id
            order by customer_id
        ) as rn

    from {{ ref('stg_customers') }}

)

select
    customer_unique_id,
    customer_id as representative_customer_id,
    customer_city,
    customer_state

from customer_records

where rn = 1