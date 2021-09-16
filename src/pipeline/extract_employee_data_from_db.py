from src.utils import *

def extract_employee_data():
    # create_table_schema('destination_employee', 'employee_timesheet_db') # create employee destination table

    source_conn = connect('employee_timesheet_db')
    dest_conn = connect('employee_timesheet_db')

    source_cursor = source_conn.cursor()
    dest_cursor = dest_conn.cursor()

    delete_existing_records('raw_destination_employee_data', 'employee_timesheet_db')

    with open('../sql/query/extract_raw_employee_data_from_db.sql') as select_file:
        select_query = "".join(select_file.readlines())
        source_cursor.execute(select_query)
        result = source_cursor.fetchall()
        
        for row in result:
            insert_query = """
                INSERT INTO raw_destination_employee_data
                VALUES (%s, %s, %s, %s, %s, %s);
            """
            dest_cursor.execute(insert_query, row)
            dest_conn.commit()

    source_conn.close()
    dest_conn.close()

if __name__ == '__main__':
    extract_employee_data()