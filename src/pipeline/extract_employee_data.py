from os import curdir
import psycopg2 as pg2
import json 
import xmltodict
from utils import *

def extract_employee_data_json(file_path, flag):
    conn = connect()
    cursor = conn.cursor()

    with open(file_path) as json_data:
        record_list = json.load(json_data)

    if flag:
        delete_existing_records('../sql/query/delete_raw_employee_data.sql')
    
    with open('../sql/query/insert_raw_employee_data_json.sql') as insert_file:
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
        delete_existing_records('../sql/query/delete_raw_employee_data.sql')
    
    record_list = data_dict["EmployeeList"]["Employee"]
    with open('../sql/query/insert_raw_employee_data_json.sql') as insert_file:
        insert_query = "".join(insert_file.readlines())
        cursor.executemany(insert_query, record_list)
        conn.commit()

    cursor.close()
    conn.close()
 
if __name__ == "__main__":
    create_table_schema('../../schema/create_raw_employee_data.sql')

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
                extract_data(path, True, '../sql/query/delete_raw_employee_data.sql', '../sql/query/insert_raw_employee_data.sql')
            else:
                extract_data(path, False, '../sql/query/delete_raw_employee_data.sql', '../sql/query/insert_raw_employee_data.sql')

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