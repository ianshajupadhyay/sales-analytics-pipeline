select
    order_id,
    seller_id,
    count(*) as item_count,
    sum(price) as product_value,
    sum(freight_value) as freight_value

from {{ ref('stg_order_items') }}

group by
    order_id,
    seller_id