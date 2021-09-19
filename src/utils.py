import psycopg2 as pg2
from dotenv import load_dotenv
import os
import json 
import xmltodict

load_dotenv()

def connect(database):
    return pg2.connect(
                host = os.getenv('HOST'),
                user = os.getenv('USER'),
                password = os.getenv('PASSWORD'),
                port = os.getenv('PORT'),
                database = database
            )

def db_connection(database):
    conn = connect(database)
    cursor = conn.cursor()
    return conn, cursor

def close_connection(conn, cursor):
    cursor.close()
    conn.close()

def create_database_table(conn, cursor, table_name, database, sql_create):
    with open(sql_create) as create_file:
        create_query = "".join(create_file.readlines())
        cursor.execute(create_query)
        conn.commit()
        print("{} table successfully created in {} database.".format(table_name, database))

def delete_table_records(conn, cursor, table_name):
    delete_query = 'TRUNCATE TABLE {}'.format(table_name)
    cursor.execute(delete_query)
    conn.commit()
    print("Successfully truncated table {}.".format(table_name))

def extract_data_from_csv(conn, cursor, file_path, table_name, sql_insert):
    with open(file_path, 'r') as file:       
        next(file)
        for line in file:
            row = line.strip().split(',')
            with open(sql_insert) as insert_file:
                insert_query = "".join(insert_file.readlines())
                cursor.execute(insert_query, row)
                conn.commit()
        print("Values successfully inserted in {} table.".format(table_name))

def extract_data_from_file(conn, cursor, file_path, table_name, sql_insert):
    file_type = file_path.split('.')[-1] # json, csv)

    if file_type == 'csv':       
        extract_data_from_csv(conn, cursor, file_path, table_name, sql_insert)

    elif file_type == 'json' or file_type == 'xml':
        xml_flag = False
        with open(file_path) as file_data:
            if file_type == 'json':
                record_list = json.load(file_data)
            elif file_type == 'xml':
                data_dict = xmltodict.parse(file_data.read())
                xml_flag = True
            
            if xml_flag: 
                record_list = data_dict["EmployeeList"]["Employee"]
        
        with open(sql_insert) as insert_file:
            insert_query = "".join(insert_file.readlines())
            cursor.executemany(insert_query, record_list)
            conn.commit()

def extract_data_from_db(source_cursor, dest_conn, dest_cursor, source_db, dest_db, sql_select, sql_insert):
    with open(sql_select) as select_file:
        select_query = "".join(select_file.readlines())
        source_cursor.execute(select_query)
        result = source_cursor.fetchall()
        
        for row in result:
            with open(sql_insert) as insert_file:
                insert_query = "".join(insert_file.readlines())
                dest_cursor.execute(insert_query, row)
                dest_conn.commit()
        print("Data successfully inserted from {} db to {} db.".format(source_db, dest_db))

