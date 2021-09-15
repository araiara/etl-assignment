from os import curdir
import psycopg2 as pg2
import json 
import xmltodict

def connect():
    return pg2.connect(
                host = "localhost",
                user = "postgres",
                password = "sql-admin",
                port = "5432",
                database = "employee_timesheet_db"
            )

def create_raw_employee_data_schema():
    conn = connect()
    cursor = conn.cursor()

    with open('../../schema/create_raw_employee_data.sql') as create_file:
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

def extract_employee_data_csv(file_path, flag):
    conn = connect()
    cursor = conn.cursor()

    with open(file_path, 'r') as file:
        if flag:
            delete_existing_records('../sql/procedure/delete_raw_employee_data.sql')

        next(file)
        for line in file:
            row = line.strip().split(',')

            with open('../sql/procedure/insert_raw_employee_data.sql') as insert_file:
                insert_query = "".join(insert_file.readlines())
                cursor.execute(insert_query, row)
                conn.commit()
    cursor.close()
    conn.close()

def extract_employee_data_json(file_path, flag):
    conn = connect()
    cursor = conn.cursor()

    with open(file_path) as json_data:
        record_list = json.load(json_data)

    if flag:
        delete_existing_records('../sql/procedure/delete_raw_employee_data.sql')
    
    with open('../sql/procedure/insert_raw_employee_data_json.sql') as insert_file:
        insert_query = "".join(insert_file.readlines())
        cursor.executemany(insert_query, record_list)
        conn.commit()
    cursor.close()
    conn.close()

def extract_employee_data_xml(file_path, flag):
    conn = connect()
    cursor = conn.cursor()

    with open(file_path) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    
    if flag:
        delete_existing_records('../sql/procedure/delete_raw_employee_data.sql')
    
    record_list = data_dict["EmployeeList"]["Employee"]
    with open('../sql/procedure/insert_raw_employee_data_json.sql') as insert_file:
        insert_query = "".join(insert_file.readlines())
        cursor.executemany(insert_query, record_list)
        conn.commit()

    cursor.close()
    conn.close()
 
if __name__ == "__main__":
    create_raw_employee_data_schema()

    selection = int(input('''
        Select the format to import from.
        1. CSV
        2. JSON
        3. XML
        Enter your choice: 
    '''))

    if selection == 1:
        employee_data_path = ['../../data/employee_2021_08_01.csv']
        for path in employee_data_path:
            if path == employee_data_path[0]:
                extract_employee_data_csv(path, True)
            else:
                extract_employee_data_csv(path, False)

    elif selection == 2:
        employee_data_path = ['../../data/employee_2021_08_01.json']
        for path in employee_data_path:
            if path == employee_data_path[0]:
                extract_employee_data_json(path, True)
            else:
                extract_employee_data_json(path, False)
                
    elif selection == 3:
        employee_data_path = ['../../data/employee_2021_08_01.xml']
        for path in employee_data_path:
            if path == employee_data_path[0]:
                extract_employee_data_xml(path, True)
            else:
                extract_employee_data_xml(path, False)
    else:
        print("Enter valid number.")