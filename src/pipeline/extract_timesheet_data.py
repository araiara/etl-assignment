from src.utils import *

def extract_timesheet_data_copy(file_path, flag):
    conn = connect('employee_timesheet_db')
    cursor = conn.cursor()

    if flag:
        delete_existing_records('raw_timesheet_data', 'employee_timesheet_db')

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
    # timesheet_data_path = ['../../data/timesheet_2021_05_23.csv', '../../data/timesheet_2021_06_23.csv', '../../data/timesheet_2021_07_24.csv']
    timesheet_data_path = ['../../data/timesheet_2021_05_23.csv']

    # F:/lf-data-engineering-internship/week-3-OLAP/assignments/data/employee_2021_08_01.csv
    for path in timesheet_data_path:
        if path == timesheet_data_path[0]:
            extract_data(path, True, 'raw_timesheet_data', 'employee_timesheet_db')
        else:
            extract_data(path, False, 'raw_timesheet_data', 'employee_timesheet_db')