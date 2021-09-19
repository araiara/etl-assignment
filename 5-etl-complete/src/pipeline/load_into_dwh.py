from extract_data_from_db import extract_data_from_db

def load_into_dwh():
    """
    Extract the data from the transformed sources.
    Load into the data warehouse.
    """
    load_dwh_info = [
        {
            'source_db': 'employee_db',
            'dest_db': 'employee_db',
            'source_table': 'employee',
            'dest_table': 'dim_role',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_role_from_employee.sql'
        },
        {
            'source_db': 'employee_db',
            'dest_db': 'employee_db',
            'source_table': 'employee',
            'dest_table': 'dim_manager',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_manager_from_employee.sql'
        },
        {
            'source_db': 'employee_db',
            'dest_db': 'employee_db',
            'source_table': 'department',
            'dest_table': 'dim_department',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_department_from_department.sql'
        },
        {
            'source_db': 'employee_db',
            'dest_db': 'employee_db',
            'source_table': 'employee',
            'dest_table': 'fact_employee',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_employee_from_employee.sql'
        },
        {
            'source_db': 'employee_db',
            'dest_db': 'employee_db',
            'source_table': 'timesheet',
            'dest_table': 'dim_shift_type',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_shift_type_from_timesheet.sql'
        },
        {
            'source_db': 'employee_db',
            'dest_db': 'employee_db',
            'source_table': 'timesheet',
            'dest_table': 'fact_timesheet',
            'sql_select': None,
            'sql_insert': '../sql/load/extract_timesheet_from_timesheet.sql'
        }
    ]

    for load_info in load_dwh_info:
        try:
            extract_data_from_db(load_info['source_db'], load_info['dest_db'], load_info['dest_table'], load_info['sql_select'], load_info['sql_insert'])
        except Exception as e:
            print("An error occurred: ", e)
        else:
            print("Successfully inserted records in {} table of {} database from {} table of {} database.".format(load_info['dest_table'], load_info['dest_db'], load_info['source_table'], load_info['source_db']))
