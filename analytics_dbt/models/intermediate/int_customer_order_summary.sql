select
    customer_unique_id,

    count(distinct order_id) as order_count,

    sum(coalesce(total_order_value, 0)) as total_order_value,

    avg(total_order_value) as average_order_value,

    min(order_purchase_timestamp) as first_order_date,

    max(order_purchase_timestamp) as last_order_date,

    case
        when count(distinct order_id) = 1 then 'One-time'
        else 'Repeat'
    end as customer_type

from (
    select
        oc.customer_unique_id,
        oc.order_id,
        oc.order_purchase_timestamp,
        ov.total_order_value

    from {{ ref('int_order_customer') }} oc

    left join {{ ref('int_order_value') }} ov
        on oc.order_id = ov.order_id
) orders

group by customer_unique_id