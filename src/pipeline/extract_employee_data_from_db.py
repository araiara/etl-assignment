import psycopg2 as pg2

def connect():
    return pg2.connect(
                host = "localhost",
                user = "postgres",
                password = "sql-admin",
                port = "5432",
                database = "employee_timesheet_db"
            )

def extract_employee_data():
    source_conn = connect()
    dest_conn = connect()

    source_cursor = source_conn.cursor()
    dest_cursor = dest_conn.cursor()

    dest_cursor.execute('DELETE FROM raw_destination_employee_data;');

    with open('../sql/procedure/extract_raw_data_from_db.sql') as select_file:
        select_query = "".join(select_file.readlines())
        source_cursor.execute(select_query)
        result = source_cursor.fetchall()
        
        for row in result:
            insert_query = """
                INSERT INTO raw_destination_employee_db
                VALUES (%s, %s, %s, %s, %s, %s);
            """
            dest_cursor.execute(insert_query, row)
            dest_conn.commit()

    source_conn.close()
    dest_conn.close()