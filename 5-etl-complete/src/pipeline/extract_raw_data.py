from src.utils.db_table import delete_table_records
from src.utils.create_connection import *

def extract_raw_data():
    """
    Extract data from csv file into raw db.
    """
    extract_from_file_info = [
        {
            'database': 'employee_db',
            'table': 'raw_employee',
            'file_path': 'F:/lf-data-engineering-internship/week-3-OLAP/5-etl-assignment/data/employee_2021_08_01.csv',
            'sql_insert': '../sql/insert/insert_raw_employee.sql'
        },
        {
            'database': 'employee_db',
            'table': 'raw_timesheet',
            'file_path': 'F:/lf-data-engineering-internship/week-3-OLAP/5-etl-assignment/data/timesheet_2021_05_23.csv',
            'sql_insert': '../sql/insert/insert_raw_timesheet.sql'
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
