INSERT INTO raw_employee_data 
VALUES 
(%(employee_id)s, %(first_name)s, %(last_name)s, %(department_id)s, %(department_name)s, %(manager_employee_id)s, %(employee_role)s, %(salary)s, %(hire_date)s, %(terminated_date)s, %(terminated_reason)s, %(dob)s, %(fte)s, %(location)s);