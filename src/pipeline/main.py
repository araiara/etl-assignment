from src.utils import *

def create_table():
    create_tables = [
        {
            'database': 'employee_timesheet',
            'tables': ['raw_employee_data', 'raw_timesheet_data', 'department', 'raw_sales_data', 'employee'],
            'sql_create': ['../../schema/create_raw_employee_data.sql', '../../schema/create_raw_timesheet_data.sql', '../../schema/create_transform_department_data.sql', '../../schema/create_raw_sales_data.sql', '../../schema/create_transform_employee_data.sql']
        }
    ]

    for create_info in create_tables:
        for index, table in enumerate(create_info['tables']):
            conn, cursor = db_connection(create_info['database'])
            create_database_table(conn, cursor, table, create_info['database'], create_info['sql_create'][index])
            delete_table_records(conn, cursor, table)
    close_connection(conn, cursor)

def extract_data_from_file_paths():
    extract_from_file_paths = [
        {
            'database': 'employee_timesheet',
            'table': 'raw_employee_data',
            'file_paths': ['../../data/employee_2021_08_01.json'],
            'sql_insert': '../sql/query/insert_raw_employee_data_json.sql'
        },
        {
            'database': 'employee_timesheet',
            'table': 'raw_employee_data',
            'file_paths': ['../../data/employee_2021_08_02.csv'],
            'sql_insert': '../sql/query/insert_raw_employee_data.sql'
        },
        {
            'database': 'employee_timesheet',
            'table': 'raw_timesheet_data',
            'file_paths': ['../../data/timesheet_2021_07_24.csv'],
            'sql_insert': '../sql/query/insert_raw_timesheet_data.sql'
        }        
    ]

    for extract_info in extract_from_file_paths:
        for file_path in extract_info['file_paths']:
            conn, cursor = db_connection(extract_info['database'])
            extract_data_from_file(conn, cursor, file_path, extract_info['table'], extract_info['sql_insert'])
    close_connection(conn, cursor)

def extract_data_from_dbs():
    extract_from_dbs = [
        {
            'source_db': 'employee_timesheet',
            'destination_db': 'employee_timesheet',
            'sql_select': '../sql/query/extract_department_data_from_raw_employee.sql',
            'sql_insert': '../sql/query/insert_department_data.sql'
        },
        {
            'source_db': 'sales_db',
            'destination_db': 'employee_timesheet',
            'sql_select': '../sql/query/extract_raw_sales_data_from_sales_db.sql',
            'sql_insert': '../sql/query/insert_raw_sales_data.sql'
        },
        {
            'source_db': 'employee_timesheet',
            'destination_db': 'employee_timesheet',
            'sql_select': '../sql/query/extract_employee_data_from_raw_data.sql',
            'sql_insert': '../sql/query/insert_employee_data.sql'
        }
    ]

    for extract_info in extract_from_dbs:
        source_conn, source_cursor = db_connection(extract_info['source_db'])
        dest_conn, dest_cursor = db_connection(extract_info['destination_db'])

        extract_data_from_db(source_cursor, dest_conn, dest_cursor, extract_info['source_db'], extract_info['destination_db'], extract_info['sql_select'], extract_info['sql_insert'])
    close_connection(source_conn, source_cursor)
    close_connection(dest_conn, dest_cursor)

def main():
    create_table()
    extract_data_from_file_paths()  
    extract_data_from_dbs() 
 
main()


