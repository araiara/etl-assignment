import psycopg2 as pg2

def connect(database):
    return pg2.connect(
                host = "localhost",
                user = "postgres",
                password = "sql-admin",
                port = "5432",
                database = database
            )

def create_table_schema(schema_name, database):
    conn = connect(database)
    cursor = conn.cursor()

    if schema_name == 'sales':
        schema_path = '../../schema/create_raw_sales_data.sql'
    elif schema_name == 'employee':
        schema_path = '../../schema/create_raw_employee_data.sql'
    elif schema_name == 'timesheet':
        schema_path = '../../schema/create_raw_timesheet_data.sql'
    elif schema_name == 'destination_employee':
        schema_path = '../../schema/create_raw_destination_employee_data.sql'
    elif schema_name == 'archive_timesheet':
        schema_path = '../../schema/create_raw_timesheet_data_archive.sql'

    with open(schema_path) as create_file:
        create_query = "".join(create_file.readlines())
        cursor.execute(create_query)
        conn.commit()
    cursor.close()
    conn.close()

def delete_existing_records(schema_name, database):
    conn = connect(database)
    cursor = conn.cursor()

    delete_query = 'TRUNCATE TABLE {}'.format(schema_name)
    cursor.execute(delete_query)
    conn.commit()

    cursor.close()
    conn.close()

def extract_data(file_path, flag, schema_name, database):
    conn = connect(database)
    cursor = conn.cursor()

    if flag:
        delete_existing_records(schema_name, database)
    
    if schema_name == 'raw_timesheet_data':
        insert_path = '../sql/query/insert_raw_timesheet_data.sql'
    elif schema_name == 'raw_employee_data':
        insert_path = '../sql/query/insert_raw_employee_data.sql'

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