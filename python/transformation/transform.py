import pandas as pd

def transform_customers(df):
    '''
    Created a copy of dataset
    asserted customer_id to be unique
    return df
    '''
    df = df.copy()
    assert df['customer_id'].is_unique
    return df

def transform_sellers(df):
    '''
        Created a copy of dataset
        asserted seller_id to be unique
        return df
    '''
    df = df.copy()
    assert df['seller_id'].is_unique
    return df

def transform_product_category_name_translation(df):
    '''
        Created a copy of dataset
        asserted product_category_name, product_category_name_english to be unique
        return df
    '''
    df = df.copy()
    assert df['product_category_name'].is_unique
    assert df['product_category_name_english'].is_unique
    return df

def transform_products(df):
    '''
        Created a copy of dataset
        asserted product_id to be unqiue
        filled product_category_name with Unknown for blank values and check that no blank values existed in this columns
        return df
    '''
    df = df.copy()
    assert df['product_id'].is_unique
    # Missing product category name are filled with "Unknown"
    df['product_category_name'] = df['product_category_name'].fillna('Unknown')
    assert df['product_category_name'].isna().sum() == 0
    return df

def transform_geolocation(df):
    '''
        Created a copy of dataset
        drop duplicates
        asserted no duplicate rowws in dataset
        return df
    '''
    df = df.copy()
    df = df.drop_duplicates()
    assert df.duplicated().sum() == 0
    return df

def transform_orders(df):
    '''
        Created a copy of dataset
        asserted order_id, customer_id is unique
        changed datatype from str to datetime for date time column and asserted it is done correctly
        return df
    '''
    df = df.copy()
    assert df['order_id'].is_unique
    assert df['customer_id'].is_unique
    columns_to_datetime = ['order_purchase_timestamp',
       'order_approved_at', 'order_delivered_carrier_date',
       'order_delivered_customer_date', 'order_estimated_delivery_date']
    for column in columns_to_datetime:
        df[column] = pd.to_datetime(df[column], errors="raise")
        assert pd.api.types.is_datetime64_any_dtype(df[column])
    return df

def transform_order_items(df):
    '''
        Created a copy of dataset
        assert composite key (order_id','order_item_id') is unqiue
        converted shipping_limit_date to datetime from str and asserted that 
        asserted price, freight_value are type numeric and is >=0 
        return df
    '''
    df = df.copy()
    assert df[['order_id','order_item_id']].duplicated().sum() == 0
    df['shipping_limit_date'] = pd.to_datetime(df['shipping_limit_date'], errors= 'raise')
    assert pd.api.types.is_datetime64_any_dtype(df['shipping_limit_date'])
    assert pd.api.types.is_any_real_numeric_dtype(df['price'])
    assert pd.api.types.is_any_real_numeric_dtype(df['freight_value'])
    assert (df['price'] >= 0).all()
    assert (df['freight_value'] >= 0).all()
    return df

def transform_order_payments(df):
    '''
        Created a copy of dataset
        assert composite key ('order_id','payment_sequential') is unqiue
        converted numberic values to numberic (in case any str is loaded) and asserted that
        asserted payment_sequential, payment_value and payment_installments values and also will log invalid rows
        return df
    '''
    df = df.copy()
    assert df[['order_id','payment_sequential']].duplicated().sum() == 0
    columns_name = ['payment_sequential', 'payment_value', 'payment_installments']
    for column in columns_name:
        df[column] = pd.to_numeric(df[column], errors= 'raise')
        assert pd.api.types.is_any_real_numeric_dtype(df[column])
    assert (df['payment_sequential'] >= 1).all()
    assert (df['payment_value'] >= 0).all()
    valid_mask = df['payment_installments'] >= 1
    invalid_payment_rows = df[~valid_mask] #Removed invalid rows from dataset as payment_installments cannot be 0 and   but there are two rows with value 0 so we move them to invalid data and only use valid data ahead
    df = df[valid_mask]
    assert (df['payment_installments'] >= 1).all()
    return df

def transform_order_reviews(df):
    '''
        Created a copy of dataset
        assert composite key ('review_id','order_id') is unqiue
        converted review_score to numberic if it is string and asserted numeric value
        converted datetime value from str to datetime and asserted that
        return df
    '''
    df = df.copy()
    assert df[['review_id','order_id']].duplicated().sum() == 0
    df['review_score'] = pd.to_numeric(df['review_score'], errors= 'raise')
    assert pd.api.types.is_any_real_numeric_dtype(df['review_score'])
    assert (df['review_score']>=1).all() and (df['review_score']<=5).all()
    column_datetypes = ['review_creation_date' , 'review_answer_timestamp']
    for column in column_datetypes:
        df[column] = pd.to_datetime(df[column])
        assert pd.api.types.is_datetime64_any_dtype(df[column])
    return df

def transform_raw_data(raw_data):
    '''
    Transform raw data dict to transformed data dictonary and return dict
    '''
    transformed_data = {}
    transformed_data['customers'] = transform_customers(raw_data['customers'])
    transformed_data['sellers'] = transform_sellers(raw_data['sellers'])
    transformed_data['product_category_name_translation'] = transform_product_category_name_translation(raw_data['product_category_name_translation'])
    transformed_data['products'] = transform_products(raw_data['products'])
    transformed_data['geolocation'] = transform_geolocation(raw_data['geolocation'])
    transformed_data['orders'] = transform_orders(raw_data['orders'])
    transformed_data['order_items'] = transform_order_items(raw_data['order_items'])
    transformed_data['order_payments'] = transform_order_payments(raw_data['order_payments'])
    transformed_data['order_reviews'] = transform_order_reviews(raw_data['order_reviews'])
    return transformed_data


