/*
product_category_name_translation
product_category_name str not null UNIQUE
product_category_name_english str not null UNIQUE
*/

CREATE TABLE staging.product_category_name_translation (
    product_category_name TEXT not null UNIQUE,
    product_category_name_english TEXT not null UNIQUE
)