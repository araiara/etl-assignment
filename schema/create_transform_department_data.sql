CREATE TABLE IF NOT EXISTS department (
    id SERIAL PRIMARY KEY,
    client_department_id VARCHAR(255) UNIQUE,
    department_name VARCHAR(255)
);