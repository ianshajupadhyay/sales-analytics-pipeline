/*
order_payments
-> order_id TEXT NOT NULL
-> payment_sequential INTEGER NOT NULL
-> payment_type TEXT NOT NULL
-> payment_installments INTEGER NOT NULL
-> payment_value NUMERIC(10,2) NOT NULL
*/ 

CREATE TABLE staging.order_payments (
    order_id TEXT NOT NULL,
    payment_sequential INTEGER NOT NULL,
    payment_type TEXT NOT NULL,
    payment_installments INTEGER NOT NULL,
    payment_value NUMERIC(10,2) NOT NULL,
    CONSTRAINT pk_order_payments 
    PRIMARY KEY(
        order_id,
        payment_sequential
    )
)