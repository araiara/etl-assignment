INSERT INTO fact_employee (
  client_employee_id, first_name, last_name, department_id, manager_id, salary, hire_date, terminated_date, terminated_reason, dob, weekly_hours, role_id
)
SELECT 
  e.client_employee_id, 
  e.first_name, 
  e.last_name,
  d.id,
  m.id,
  e.salary ,
  e.hire_date,
  e.terminated_date,
  e.terminated_reason,
  e.dob,
  e.weekly_hours,
  r.id
FROM employee e 
LEFT JOIN dim_manager m 
  ON m.client_employee_id = e.manager_employee_id
INNER JOIN dim_role r 
  ON e.role = r.role_name
INNER JOIN dim_department d 
  ON e.department_id = d.client_department_id
ORDER BY e.id;
