from extract_data_from_db import extract_data_from_db

def transform_from_raw_data():
    """
    Extract the raw data from the source tables.
    Transform and extract into the destination tables.
    """
    extract_from_db_info = [
        {
            'source_db': 'ecommerce_db',
            'dest_db': 'ecommerce_db',
            'source_table': 'raw_customer',
            'dest_table': 'customer',
            'sql_select': None,
            'sql_insert': '../sql/transform/extract_customer_from_raw_data.sql'
        },
        {
            'source_db': 'ecommerce_db',
            'dest_db': 'ecommerce_db',
            'source_table': 'raw_product',
            'dest_table': 'product',
            'sql_select': None,
            'sql_insert': '../sql/transform/extract_product_from_raw_data.sql'
        },
        {
            'source_db': 'ecommerce_db',
            'dest_db': 'ecommerce_db',
            'source_table': 'raw_sales',
            'dest_table': 'bill',
            'sql_select': None,
            'sql_insert': '../sql/transform/extract_bill_from_raw_data.sql'
        },
        {
            'source_db': 'ecommerce_db',
            'dest_db': 'ecommerce_db',
            'source_table': 'raw_sales',
            'dest_table': 'sales',
            'sql_select': None,
            'sql_insert': '../sql/transform/extract_sales_from_raw_data.sql'
        }
    ]

    for extract_info in extract_from_db_info:
        try:
            extract_data_from_db(extract_info['source_db'], extract_info['dest_db'], extract_info['dest_table'], extract_info['sql_select'], extract_info['sql_insert'])
        except Exception as e:
            print("An error occurred: ", e)
        else:
            print("Successfully inserted records in {} table of {} database from {} table of {} database.".format(extract_info['dest_table'], extract_info['dest_db'], extract_info['source_table'], extract_info['source_db']))
