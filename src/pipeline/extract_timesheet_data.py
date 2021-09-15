import psycopg2 as pg2

def connect():
    return pg2.connect(
                host = "localhost",
                user = "postgres",
                password = "sql-admin",
                port = "5432",
                database = "employee_timesheet_db"
            )

# from src.utils import connect

def create_raw_timesheet_data_schema():
    conn = connect()
    cursor = conn.cursor()

    with open('../../schema/create_raw_timesheet_data.sql') as create_file:
        create_query = "".join(create_file.readlines())
        cursor.execute(create_query)
        conn.commit()
    cursor.close()
    conn.close()

def delete_existing_records(file_path):
    conn = connect()
    cursor = conn.cursor()
    with open(file_path) as delete_file:
        delete_query = "".join(delete_file.readlines())
        cursor.execute(delete_query)
        conn.commit()
    cursor.close()
    conn.close()

def extract_timesheet_data(file_path, flag):
    conn = connect()
    cursor = conn.cursor()

    with open(file_path, 'r') as file:
        if flag:
            delete_existing_records('../sql/procedure/delete_raw_timesheet_data.sql')

        next(file)
        for line in file:
            row = line.strip().split(',')

            with open('../sql/procedure/insert_raw_timesheet_data.sql') as insert_file:
                insert_query = "".join(insert_file.readlines())
                cursor.execute(insert_query, row)
                conn.commit()
    cursor.close()
    conn.close()

def extract_timesheet_data_copy(file_path, flag):
    conn = connect()
    cursor = conn.cursor()

    if flag:
        delete_existing_records('../sql/procedure/delete_raw_timesheet_data.sql')

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
    create_raw_timesheet_data_schema()

    timesheet_data_path = ['../../data/timesheet_2021_05_23.csv', '../../data/timesheet_2021_06_23.csv', '../../data/timesheet_2021_07_24.csv']
    
    for path in timesheet_data_path:
        if path == timesheet_data_path[0]:
            extract_timesheet_data(path, True)
        else:
            extract_timesheet_data(path, False)