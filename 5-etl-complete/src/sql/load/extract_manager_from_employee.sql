INSERT INTO dim_manager(client_employee_id, first_name, last_name)
SELECT DISTINCT m.manager_employee_id, m.first_name, m.last_name
FROM employee m
INNER JOIN employee e
  ON m.manager_employee_id = e.client_employee_id;
