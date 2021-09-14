import psycopg2 as pg2

def connect():
    return pg2.connect(
                host = "localhost",
                user = "postgres",
                password = "sql-admin",
                port = "5432",
                database = "employee_timesheet_db"
            )

def extract_timesheet_data(file_path):
    conn = connect()
    cursor = conn.cursor()

    with open(file_path, 'r') as file:

        delete_query = "DELETE FROM raw_timesheet_data;"
        cursor.execute(delete_query)
        conn.commit()

        next(file)
        for line in file:
            row = line.strip().split(',')

            with open('../sql/procedure/insert_timesheet_data.sql') as insert_file:
                insert_query = "".join(insert_file.readlines())
                cursor.execute(insert_query, row)
                conn.commit()
    cursor.close()
    conn.close()

# def extract_timesheet_data_copy(file_path):
#     conn = connect()
#     cursor = conn.cursor()

#     delete_query = "DELETE FROM raw_timesheet_data;"
#     cursor.execute(delete_query)
#     conn.commit()

#     copy_query = '''
#         copy raw_timesheet_data
#         FROM %s
#         WITH (
#             FORMAT TEXT,
#             DELIMITER ','
#         );
#     '''

#     cursor.execute(copy_query, (file_path,))
#     conn.commit()
#     cursor.close()
#     conn.close()
    
if __name__ == "__main__":
    timesheet_data_path = ['../../data/timesheet_2021_05_23.csv']
    
    for path in timesheet_data_path:
        extract_timesheet_data(path)
