import psycopg2 as pg2

def connect():
    return pg2.connect(
                host = "localhost",
                user = "postgres",
                password = "sql-admin",
                port = "5432",
                database = "employee_timesheet_db"
            )

def create_table_schema(schema_path):
    conn = connect()
    cursor = conn.cursor()

    with open(schema_path) as create_file:
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

def extract_data(file_path, flag, delete_path, insert_path):
    conn = connect()
    cursor = conn.cursor()

    if flag:
        delete_existing_records(delete_path)

    with open(file_path, 'r') as file:       
        next(file)
        for line in file:
            row = line.strip().split(',')

            with open(insert_path) as insert_file:
                insert_query = "".join(insert_file.readlines())
                cursor.execute(insert_query, row)
                conn.commit()
    cursor.close()
    conn.close()