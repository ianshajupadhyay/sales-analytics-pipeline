import pandas as pd

def stage_customer(df):
    '''
    Standadize the customer dataset for staging layer
    Trim white space
    Converting customer_state to Upper case
    Converting customer_city to title case
    ''' 
    df = df.copy()
    df['customer_city'] = df['customer_city'].str.strip().str.title()
    df['customer_state'] = df['customer_state'].str.strip().str.upper()
    return df

def stage_seller(df):
    '''
    Standadize the sellers dataset for staging layer
    Trim white space
    Converting seller_city to title case
    Converting seller_state to Upper case
    ''' 
    df = df.copy()
    df['seller_city'] = df['seller_city'].str.strip().str.title()
    df['seller_state'] = df['seller_state'].str.strip().str.upper()
    return df

def stage_product_category_name_translation(df):
    '''
    Standadize the product_category_name_translation for staging layer
    Trim white space
    ''' 
    df = df.copy()
    df['product_category_name'] = df['product_category_name'].str.strip()
    df['product_category_name_english'] = df['product_category_name_english'].str.strip()
    return df

def stage_products(df):
    '''
    Standadize the product_category_name for staging layer
    Trim white space
    ''' 
    df = df.copy()
    df['product_category_name'] = df['product_category_name'].str.strip()
    columns_int = ['product_name_lenght',
       'product_description_lenght', 'product_photos_qty', 'product_weight_g',
       'product_length_cm', 'product_height_cm', 'product_width_cm']
    for col in columns_int:
        df[columns_int] = df[columns_int].astype("Int64")

    return df

def stage_geolocation(df):
    '''
        Standadize the geolocation for staging layer
        Trim white space
    ''' 
    df = df.copy()
    df['geolocation_city'] = df['geolocation_city'].str.strip().str.title()
    df['geolocation_state'] = df['geolocation_state'].str.strip().str.upper()
    return df

def stage_orders(df):
    '''
        Standadize the geolocation for staging layer
        Trim white space, title case for status
    ''' 
    df = df.copy()
    df['order_status'] = df['order_status'].str.strip().str.title()
    return df


def stage_order_items(df):
    df = df.copy()
    return df


def stage_order_payments(df):
    '''
        Standadize the order_payments for staging layer
        Trim white space, title case for payment_type
    '''
    df = df.copy()
    df['payment_type'] = df['payment_type'].str.strip().str.title()
    return df

def stage_order_reviews(df):
    '''
        Standadize the order_payments for staging layer
        Trim white space, title case for payment_type
    '''
    df = df.copy()
    df['review_comment_title'] = df['review_comment_title'].str.strip()
    df['review_comment_message'] = df['review_comment_message'].str.strip()
    return df

def stage_raw_data(transformed_data):
    '''
    Create consistent namings
    Create all to snake_case
    No new business columns
    '''
    stage_data: dict[str, pd.DataFrame] = {}
    stage_data['customers'] = stage_customer(transformed_data['customers'])
    stage_data['sellers'] = stage_seller(transformed_data['sellers'])
    stage_data['product_category_name_translation'] = stage_product_category_name_translation(transformed_data['product_category_name_translation'])
    stage_data['products'] = stage_products(transformed_data['products'])
    stage_data['geolocation'] = stage_geolocation(transformed_data['geolocation'])
    stage_data['orders'] = stage_orders(transformed_data['orders'])
    stage_data['order_items'] = stage_order_items(transformed_data['order_items'])
    stage_data['order_payments'] = stage_order_payments(transformed_data['order_payments'])
    stage_data['order_reviews'] = stage_order_reviews(transformed_data['order_reviews'])
    return stage_data