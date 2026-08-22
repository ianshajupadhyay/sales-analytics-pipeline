select 
    order_id, 
    sum(price) as product_value,
    sum(freight_value) as freight_value,
    sum(price+freight_value) as total_order_value,
    count(order_item_id) as item_count
from {{ ref('stg_order_items') }}
group by order_id  