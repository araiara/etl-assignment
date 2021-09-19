INSERT INTO dim_department(client_department_id, department_name)
SELECT client_department_id, department_name 
FROM department;
