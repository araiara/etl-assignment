from src.utils.create_connection import *
from src.utils.db_table import *
from extract_raw_data import *
from extract_archive_data import *
from transform_from_raw_data import *
from load_into_dwh import *

def create_tables():
    create_table_info = [
        {
            'database': 'employee_db',
            'tables': ['raw_employee', 'raw_timesheet', 'raw_employee_archive', 'raw_timesheet_archive'],
            'sql_create': [
                '../../schema/raw/create_raw_employee.sql',
                '../../schema/raw/create_raw_timesheet.sql',
                '../../schema/archive/create_raw_employee_archive.sql',
                '../../schema/archive/create_raw_timesheet_archive.sql'
            ]
        },
        {
            'database': 'employee_db',
            'tables': ['department', 'employee', 'timesheet'],
            'sql_create': [
                '../../schema/transform/create_department.sql',
                '../../schema/transform/create_employee.sql',
                '../../schema/transform/create_timesheet.sql'
            ]
        },
        {
            'database': 'employee_db',
            'tables': ['dim_role', 'dim_manager', 'dim_department', 'fact_employee', 'dim_shift_type', 'fact_timesheet'],
            'sql_create': [
                '../../schema/dimension/create_dim_role.sql',
                '../../schema/dimension/create_dim_manager.sql',
                '../../schema/dimension/create_dim_department.sql',
                '../../schema/fact/create_fact_employee.sql',
                '../../schema/dimension/create_dim_shift_type.sql',
                '../../schema/fact/create_fact_timesheet.sql',
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
        except Exception:
            print("An error has occured.")

def main():
    create_tables()
    # extract_raw_data()
    # extract_archive_data()
    # transform_from_raw_data()
    load_into_dwh()

main()
