SELECT
employee_id AS client_employee_id,
INITCAP(first_name) AS first_name,
INITCAP(last_name) AS last_name,
d.client_department_id AS department_id,
(CASE WHEN manager_employee_id = '-' 
 THEN NULL
 ELSE manager_employee_id END) AS manager_employee_id,
CAST(salary AS FLOAT) AS salary,
CAST(hire_date as DATE),
CAST(
	CASE WHEN terminated_date = '01-01-1700' 
	THEN NULL
	ELSE terminated_date END AS DATE
),
terminated_reason,
CAST(dob AS DATE) AS dob,
CAST(fte AS FLOAT) AS fte,
CAST(fte AS FLOAT) * 40 AS weekly_hours,
(CASE WHEN employee_role LIKE '%Mgr%' 
OR employee_role LIKE '%Supv%' 
THEN 'Manager'
ELSE 'Employee' END) AS role
FROM raw_employee_data r
JOIN department d
ON r.department_id = d.client_department_id;
