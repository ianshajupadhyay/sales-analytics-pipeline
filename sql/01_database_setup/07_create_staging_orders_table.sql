/*
orders
order_id                         TEXT NOT NULL
customer_id                      TEXT NOT NULL
order_status                     TEXT NOT NULL
order_purchase_timestamp         TIMESTAMP NOT NULL
order_approved_at                TIMESTAMP 
order_delivered_carrier_date     TIMESTAMP 
order_delivered_customer_date    TIMESTAMP
order_estimated_delivery_date    TIMESTAMP NOT NULL
*/ 

CREATE TABLE staging.orders (
order_id TEXT NOT NULL,
customer_id TEXT NOT NULL UNIQUE,
order_status TEXT NOT NULL,
order_purchase_timestamp TIMESTAMP NOT NULL,
order_approved_at TIMESTAMP,
order_delivered_carrier_date TIMESTAMP,
order_delivered_customer_date TIMESTAMP,
order_estimated_delivery_date TIMESTAMP NOT NULL,
CONSTRAINT pk_primary_key 
    PRIMARY KEY(
        order_id
    )
)