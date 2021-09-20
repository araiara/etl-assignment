from src.utils.db_table import delete_table_records
from src.utils.create_connection import *

def extract_data_from_file():
    """
    Extract data from csv file into raw db.
    """
    extract_from_file_info = [
        {
            'database': 'ecommerce_db',
            'table': 'raw_customer',
            'file_path': 'F:/lf-data-engineering-internship/week-3-OLAP/weekend-assignment/data/customer_dump.csv',
            'sql_insert': '../sql/insert/insert_raw_customer.sql'
        },
        {
            'database': 'ecommerce_db',
            'table': 'raw_product',
            'file_path': 'F:/lf-data-engineering-internship/week-3-OLAP/weekend-assignment/data/product_dump.csv',
            'sql_insert': '../sql/insert/insert_raw_product.sql'
        },
        {
            'database': 'ecommerce_db',
            'table': 'raw_sales',
            'file_path': 'F:/lf-data-engineering-internship/week-3-OLAP/weekend-assignment/data/sales_dump.csv',
            'sql_insert': '../sql/insert/insert_raw_sales.sql'
        }
    ]

    for extract_info in extract_from_file_info:
        try:
            conn, cursor = connect(extract_info['database'])    
        
            delete_table_records(conn, cursor, extract_info['table'])
            print("Successfully deleted the existing table records from {}.".format(extract_info['table']))

            with open(extract_info['sql_insert']) as insert_file:
                insert_query = "".join(insert_file.readlines())
                cursor.execute(insert_query, (extract_info['file_path'],))
                conn.commit()
                print("Successfully inserted records in {} table.".format(extract_info['table']))
        except Exception as e:
            print("An error has occurred: ", e)          
