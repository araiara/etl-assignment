import psycopg2 as pg2

try:
    connection = pg2.connect(
        host = "localhost",
        user = "postgres",
        password = "sql-admin",
        port = "5432",
        database = "employee_timesheet_db"
    )

    cursor = connection.cursor()

    create_employee_query = '''
        CREATE TABLE IF NOT EXISTS employee_dimension (
            employee_id SERIAL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            manager_employee_id INT,
            hire_date DATE NOT NULL,
            terminated_date DATE,
            terminated_reason TEXT,
            dob DATE NOT NULL,
            location TEXT NOT NULL,
            cost_center INT NOT NULL,
            CONSTRAINT pk_employee_id 
                PRIMARY KEY (employee_id),
            CONSTRAINT fk_employee_manager_employee_id
                FOREIGN KEY (manager_employee_id)
                    REFERENCES employee_dimension(employee_id)
        );
    '''
    create_department_query = '''
        CREATE TABLE IF NOT EXISTS department_dimension (
            department_id SERIAL,
            department_name TEXT NOT NULL,
            CONSTRAINT pk_department_id
                PRIMARY KEY (department_id)
        );
    '''
    create_time_query = '''
        CREATE TABLE IF NOT EXISTS time_dimension (
            time_id SERIAL,
            year INT NOT NULL,
            month INT NOT NULL,
            day INT NOT NULL,
            week INT NOT NULL,
            week_day VARCHAR(5) NOT NULL,
            punch_in_time TIME,
            punch_out_time TIME,	
            CONSTRAINT pk_time_id
                PRIMARY KEY (time_id)
        );
    '''
    create_status_query = '''
        CREATE TABLE IF NOT EXISTS status_dimension (
            status_id SERIAL,
            pay_code VARCHAR(10) NOT NULL,	
            CONSTRAINT pk_status_id
                PRIMARY KEY (status_id)
        );
    '''
    create_shift_query = '''
        CREATE TABLE IF NOT EXISTS shift_dimension (
            shift_id SERIAL,
            shift_name VARCHAR(10) NOT NULL,
            start_time TIME NOT NULL,
            end_time TIME NOT NULL,
            CONSTRAINT pk_shift_id
                PRIMARY KEY (shift_id)
        );
    '''
    create_role_query = '''
        CREATE TABLE IF NOT EXISTS role_dimension (
            role_id SERIAL,
            employee_role TEXT NOT NULL,
            CONSTRAINT pk_role_id
                PRIMARY KEY (role_id)
        );
    '''
    create_employee_timesheet_query = '''
        CREATE TABLE IF NOT EXISTS employee_timesheet_fact (
            employee_id INT,
            department_id INT,
            role_id INT, 
            shift_id INT,
            time_id INT,
            status_id INT,
            salary INT NOT NULL,
            fte FLOAT NOT NULL,
            hours_worked FLOAT NOT NULL,
            CONSTRAINT pk_employee_timesheet
                PRIMARY KEY (employee_id, department_id, role_id, shift_id, time_id, status_id)
        );
    '''

    cursor.execute(create_employee_query)
    cursor.execute(create_department_query)
    cursor.execute(create_time_query)
    cursor.execute(create_status_query)
    cursor.execute(create_shift_query)
    cursor.execute(create_role_query)
    cursor.execute(create_employee_timesheet_query)    
    
    connection.commit()

except Exception as e:
    print("An error has occured", e)

else:
    print("Successfully executed the queries.")

finally:
    cursor.close()
    connection.close()