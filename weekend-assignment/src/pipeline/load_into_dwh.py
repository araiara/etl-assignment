from extract_data_from_db import extract_data_from_db

def load_into_dwh():
    """
    Extract the data from the transformed sources.
    Load into the data warehouse.
    """
    load_dwh_info = [
        {
            'source_db': 'ecommerce_db',
            'dest_db': 'ecommerce_db',
            'source_table': 'customer',
            'dest_table': 'dim_location',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_location.sql'
        },
        {
            'source_db': 'ecommerce_db',
            'dest_db': 'ecommerce_db',
            'source_table': 'customer',
            'dest_table': 'dim_customer',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_customer.sql'
        },
        {
            'source_db': 'ecommerce_db',
            'dest_db': 'ecommerce_db',
            'source_table': 'product',
            'dest_table': 'dim_category',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_category.sql'
        },
        {
            'source_db': 'ecommerce_db',
            'dest_db': 'ecommerce_db',
            'source_table': 'product',
            'dest_table': 'dim_product',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_product.sql'
        },
        {
            'source_db': 'ecommerce_db',
            'dest_db': 'ecommerce_db',
            'source_table': 'bill',
            'dest_table': 'dim_bill',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_bill.sql'
        },
        {
            'source_db': 'ecommerce_db',
            'dest_db': 'ecommerce_db',
            'source_table': 'sales',
            'dest_table': 'fact_sales',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_sales.sql'
        }
    ]

    for load_info in load_dwh_info:
        try:
            extract_data_from_db(load_info['source_db'], load_info['dest_db'], load_info['dest_table'], load_info['sql_select'], load_info['sql_insert'])
        except Exception as e:
            print("An error occurred: ", e)
        else:
            print("Successfully inserted records in {} table of {} database from {} table of {} database.".format(load_info['dest_table'], load_info['dest_db'], load_info['source_table'], load_info['source_db']))
