from src.utils import *
from extract_timesheet_data_archive import *

def extract_timesheet_data_copy(file_path, flag, schema_name, database):
    conn = connect(database)
    cursor = conn.cursor()

    if flag:
        delete_existing_records(schema_name, database)

    copy_query = '''
        COPY raw_timesheet_data
        FROM %s
        DELIMITER ','
        CSV HEADER;
    '''

    cursor.execute(copy_query, (file_path,))
    conn.commit()
    cursor.close()
    conn.close()
 
if __name__ == "__main__":
    # timesheet_data_path = ['../../data/timesheet_2021_05_23.csv', '../../data/timesheet_2021_06_23.csv', '../../data/timesheet_2021_07_24.csv']
    timesheet_data_path = ['F:/lf-data-engineering-internship/week-3-OLAP/assignments/data/timesheet_2021_05_23.csv', 'F:/lf-data-engineering-internship/week-3-OLAP/assignments/data/timesheet_2021_06_23.csv']

    file_name = ['timesheet_2021_05_23.csv', 'timesheet_2021_06_23.csv']
    i = 0
    for index, path in enumerate(timesheet_data_path):
        if i == 0:
            extract_timesheet_data_copy(path, True, 'raw_timesheet_data', 'employee_timesheet_db')
            i += 1
        else:
            extract_timesheet_data_copy(path, False, 'raw_timesheet_data', 'employee_timesheet_db')
        extract_timesheet_data(file_name[index])

        # if path == timesheet_data_path[0]:
        #     extract_data(path, True, 'raw_timesheet_data', 'employee_timesheet_db')
        # else:
        #     extract_data(path, False, 'raw_timesheet_data', 'employee_timesheet_db')