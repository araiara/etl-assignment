import psycopg2 as pg2

def connect():
    return pg2.connect(
                host = "localhost",
                user = "postgres",
                password = "sql-admin",
                port = "5432",
                database = "employee_timesheet_db"
            )