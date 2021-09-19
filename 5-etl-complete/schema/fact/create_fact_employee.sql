CREATE TABLE IF NOT EXISTS fact_employee (
  id SERIAL PRIMARY KEY,
  client_employee_id VARCHAR(255),
  first_name VARCHAR(255),
  last_name VARCHAR(255),
  department_id INT,
  manager_id INT,
  salary FLOAT,
  hire_date DATE,
  terminated_date DATE,
  terminated_reason VARCHAR(255),
  dob DATE,
  weekly_hours FLOAT,
  role_id INT,
  CONSTRAINT fk_fact_employee_department_id
    FOREIGN KEY (department_id)
    REFERENCES dim_department(id) 
    ON DELETE CASCADE,
  CONSTRAINT fk_fact_employee_manager_id
    FOREIGN KEY (manager_id)
    REFERENCES dim_manager(id) 
    ON DELETE CASCADE,
  CONSTRAINT fk_fact_employee_role_id
    FOREIGN KEY (role_id)
    REFERENCES dim_role(id) 
    ON DELETE CASCADE
);
