from src.utils.create_connection import *
from src.utils.db_table import *
from extract_raw_data import *
from extract_archive_data import *
from transform_from_raw_data import *
from load_into_dwh import *

def create_tables():
    create_table_info = [
        {
            'database': 'ecommerce_db',
            'tables': ['raw_customer', 'raw_product', 'raw_sales', 'raw_customer_archive', 'raw_product_archive', 'raw_sales_archive'],
            'sql_create': [
                '../../schema/raw/create_raw_customer.sql',
                '../../schema/raw/create_raw_product.sql',
                '../../schema/raw/create_raw_sales.sql',
                '../../schema/archive/create_raw_customer_archive.sql',
                '../../schema/archive/create_raw_product_archive.sql',
                '../../schema/archive/create_raw_sales_archive.sql'
            ]
        },
        {
            'database': 'ecommerce_db',
            'tables': ['customer', 'product', 'bill', 'sales'],
            'sql_create': [
                '../../schema/transform/create_customer.sql',
                '../../schema/transform/create_product.sql',
                '../../schema/transform/create_bill.sql',
                '../../schema/transform/create_sales.sql'
            ]
        },
        {
            'database': 'ecommerce_db',
            'tables': ['dim_location', 'dim_customer', 'dim_category', 'dim_product', 'dim_bill', 'fact_sales'],
            'sql_create': [
                '../../schema/dimension/create_dim_location.sql',
                '../../schema/dimension/create_dim_customer.sql',
                '../../schema/dimension/create_dim_category.sql',
                '../../schema/dimension/create_dim_product.sql',
                '../../schema/dimension/create_dim_bill.sql',
                '../../schema/fact/create_fact_sales.sql',
            ]
        }
    ]

    for create_info in create_table_info:
        try:
            conn, cursor = connect(create_info['database'])
            for index, sql_create in enumerate(create_info['sql_create']):
                create_table(conn, cursor, sql_create)
                print("{} table successfully created in {} database.".format(create_info['tables'][index], create_info['database']))
            close_connection(conn, cursor)
        except Exception as e:
            print("An error has occured.", e)

def main():
    create_tables()
    extract_data_from_file()
    extract_archive_data()
    transform_from_raw_data()
    load_into_dwh()

main()
