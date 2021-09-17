CREATE TABLE IF NOT EXISTS department (
    id SERIAL PRIMARY KEY,
    client_department_id VARCHAR(255),
    department_name VARCHAR(255)
);