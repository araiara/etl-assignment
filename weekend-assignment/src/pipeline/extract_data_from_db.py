from src.utils.db_table import delete_table_records
from src.utils.create_connection import *

def extract_data_from_db(source_db, dest_db, dest_table, sql_select, sql_insert):
    """
    Extract data from one db to another.
    params:
    param 'source_db' name of the source database
    type 'string'
    param 'dest_db' name of the destination database
    type 'string'
    param 'dest_table' name of the destination table
    type 'string'
    param 'sql_select' path to the sql file consisting select command
    type 'string'
    param 'sql_insert' path to the sql file consisting insert command
    type 'string'
    """

    dest_conn, dest_cursor = connect(dest_db)    

    delete_table_records(dest_conn, dest_cursor, dest_table)
    print("Successfully deleted the existing records from {} destination table.".format(dest_table))

    if source_db == dest_db:              
        with open(sql_insert) as insert_file:
            insert_query = "".join(insert_file.readlines())
            dest_cursor.execute(insert_query)
            dest_conn.commit()

    else:
        source_conn, source_cursor = connect(source_db)

        with open(sql_select) as select_file:
            select_query = "".join(select_file.readlines())
            source_cursor.execute(select_query)
            result = source_cursor.fetchall()
            
            for row in result:
                with open(sql_insert) as insert_file:
                    insert_query = "".join(insert_file.readlines())
                    dest_cursor.execute(insert_query, row)
                    dest_conn.commit()
        close_connection(source_conn, source_cursor)
    close_connection(dest_conn, dest_cursor)
