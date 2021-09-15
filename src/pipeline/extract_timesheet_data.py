import psycopg2 as pg2
from utils import *

# from ..utils import connect

def extract_timesheet_data_copy(file_path, flag):
    conn = connect()
    cursor = conn.cursor()

    if flag:
        delete_existing_records('../sql/query/delete_raw_timesheet_data.sql')

    copy_query = '''
        COPY raw_timesheet_data
        FROM %s
        WITH (
            FORMAT TEXT,
            DELIMITER ','
        );
    '''

    cursor.execute(copy_query, (file_path,))
    conn.commit()
    cursor.close()
    conn.close()
 
if __name__ == "__main__":
    create_table_schema('../../schema/create_raw_timesheet_data.sql')

    # timesheet_data_path = ['../../data/timesheet_2021_05_23.csv', '../../data/timesheet_2021_06_23.csv', '../../data/timesheet_2021_07_24.csv']
    timesheet_data_path = ['../../data/timesheet_2021_05_23.csv']

    for path in timesheet_data_path:
        if path == timesheet_data_path[0]:
            extract_data(path, True, '../sql/query/delete_raw_timesheet_data.sql', '../sql/query/insert_raw_timesheet_data.sql')
        else:
            extract_data(path, False, '../sql/query/delete_raw_timesheet_data.sql', '../sql/query/insert_raw_timesheet_data.sql')