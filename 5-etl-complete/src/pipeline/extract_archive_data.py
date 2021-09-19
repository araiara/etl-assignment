from extract_data_from_db import extract_data_from_db

def extract_archive_data():
    """
    Extract the raw data from the source tables to the destination archive table.
    """
    extract_from_db_info = [
        {
            'source_db': 'employee_db',
            'dest_db': 'employee_db',
            'source_table': 'raw_employee',
            'dest_table': 'raw_employee_archive',
            'sql_select': None,
            'sql_insert': '../sql/insert/insert_raw_employee_archive.sql'
        },
        {
            'source_db': 'employee_db',
            'dest_db': 'employee_db',
            'source_table': 'raw_timesheet',
            'dest_table': 'raw_timesheet_archive',
            'sql_select': None,
            'sql_insert': '../sql/insert/insert_raw_timesheet_archive.sql'
        }
    ]

    for extract_info in extract_from_db_info:
        try:
            extract_data_from_db(extract_info['source_db'], extract_info['dest_db'], extract_info['dest_table'], extract_info['sql_select'], extract_info['sql_insert'])
        except Exception as e:
            print("An error occurred: ", e)
        else:
            print("Successfully inserted records in {} table of {} database from {} table of {} database.".format(extract_info['dest_table'], extract_info['dest_db'], extract_info['source_table'], extract_info['source_db']))
