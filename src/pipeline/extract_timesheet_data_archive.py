from src.utils import *

def extract_timesheet_data(flag, file_name):
    # create_table_schema('archive_timesheet', 'employee_timesheet_db') # create employee destination table

    source_conn = connect('employee_timesheet_db')
    dest_conn = connect('employee_timesheet_db')

    source_cursor = source_conn.cursor()
    dest_cursor = dest_conn.cursor()

    if flag:
        delete_existing_records('raw_timesheet_data_archive', 'employee_timesheet_db')

    with open('../sql/query/extract_raw_timesheet_data_archive_from_db.sql') as select_file:
        select_query = "".join(select_file.readlines())
        source_cursor.execute(select_query)
        result = source_cursor.fetchall()
        
        for row in result:
            list_row = list(row)
            list_row.append(file_name)

            insert_query = """
                INSERT INTO raw_timesheet_data_archive
                (employee_id, cost_center, punch_in_time, punch_out_time, punch_apply_date, hours_worked, paycode, file_name)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """

            dest_cursor.execute(insert_query, list_row)
            dest_conn.commit()

    source_conn.close()
    dest_conn.close()

# if __name__ == "__main__":
#     extract_timesheet_data()