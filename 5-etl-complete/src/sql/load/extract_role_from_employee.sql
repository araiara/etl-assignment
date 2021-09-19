INSERT INTO dim_role (role_name)
SELECT
DISTINCT role
FROM employee;
