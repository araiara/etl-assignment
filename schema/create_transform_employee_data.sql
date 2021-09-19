CREATE TABLE IF NOT EXISTS employee (
    id SERIAL PRIMARY KEY,
    client_employee_id VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    department_id VARCHAR(255),
    manager_employee_id VARCHAR(255),
    salary FLOAT,
    hire_date DATE,
    terminated_date DATE,
    terminated_reason VARCHAR(255),
    dob DATE,
    fte FLOAT,
    weekly_hours FLOAT,
    role VARCHAR(255),
    CONSTRAINT fk_employee_department_id
    FOREIGN KEY (department_id)
    REFERENCES department(client_department_id)
);
