select 
    product_category_name,
    product_category_name_english
from {{ source('staging','product_category_name_translation') }}