from src.utils import *

def extract_sales_data():
    # create_table_schema('sales', 'sales_db') # create sales table

    source_conn = connect('sales_db')
    dest_conn = connect('sales_db')

    source_cursor = source_conn.cursor()
    dest_cursor = dest_conn.cursor()

    delete_existing_records('raw_sales_data', 'sales_db')
    
    with open('../sql/query/extract_raw_sales_data_from_db.sql') as select_file:
        select_query = "".join(select_file.readlines())
        source_cursor.execute(select_query)
        result = source_cursor.fetchall()
        
        for row in result:
            insert_query = """
                INSERT INTO raw_sales_data
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
            """
            dest_cursor.execute(insert_query, row)
            dest_conn.commit()

    source_conn.close()
    dest_conn.close()

if __name__ == '__main__':
    extract_sales_data()
