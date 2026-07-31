/*
Sellers
seller_id Text
seller_zip_code_prefix TEXT
seller_city TEXT
seller_state VARCHAR(2)
*/

create table staging.sellers (
    seller_id Text NOT NULL,
    seller_zip_code_prefix Text NOT NULL,
    seller_city Text NOT NULL,
    seller_state VARCHAR(2)  NOT NULL,
    CONSTRAINT pk_sellers PRIMARY KEY (
        seller_id
    )
)