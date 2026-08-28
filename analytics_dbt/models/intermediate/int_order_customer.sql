select 
    a.order_id, 
    a.customer_id as customer_id,
    b.customer_unique_id,
    b.customer_city,
    b.customer_state,
    a.order_status,
    a.order_purchase_timestamp,
    a.order_approved_at,
    a.order_delivered_carrier_date,
    a.order_delivered_customer_date,
    a.order_estimated_delivery_date 

from {{ ref('stg_orders') }} a
left join {{ ref('stg_customers') }} b
on a.customer_id = b.customer_id
