INSERT INTO dim_shift_type (shift_name)
SELECT
DISTINCT shift_type
FROM timesheet;
