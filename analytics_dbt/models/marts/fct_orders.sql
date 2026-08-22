select
    oc.order_id,
    oc.customer_id,
    oc.customer_unique_id,
    oc.order_status,
    oc.order_purchase_timestamp,
    oc.order_approved_at,
    oc.order_delivered_carrier_date,
    oc.order_delivered_customer_date,
    oc.order_estimated_delivery_date,
    coalesce(ov.product_value, 0) as product_value,
    coalesce(ov.freight_value, 0) as freight_value,
    coalesce(ov.total_order_value, 0) as total_order_value,
    coalesce(ov.item_count, 0) as item_count,

    ps.total_payment_value,
    ps.payment_count,

    case
        when oc.order_delivered_customer_date is null
            then null

        when oc.order_delivered_customer_date
             > oc.order_estimated_delivery_date
            then 'Late'

        else 'On Time'
    end as delivery_status

from {{ ref('int_order_customer') }} oc

left join {{ ref('int_order_value') }} ov
    on oc.order_id = ov.order_id

left join {{ ref('int_order_payments_summary') }} ps
    on oc.order_id = ps.order_id