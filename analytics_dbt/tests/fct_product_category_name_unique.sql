select
    product_category_name,
    count(*) as row_count
from {{ ref('stg_product_category_name_translation') }}
group by product_category_name
having count(*) > 1 