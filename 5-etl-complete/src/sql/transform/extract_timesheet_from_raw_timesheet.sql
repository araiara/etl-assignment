INSERT INTO timesheet(client_employee_id, client_department_id, shift_start_time, shift_end_time, shift_date, shift_type, hours_worked, attendance, has_taken_break, break_hour, was_charge, charge_hour, was_on_call, on_call_hour)
SELECT
e.client_employee_id,
e.department_id,
CASE WHEN punch_in_time = '' 
  THEN NULL
ELSE 
  CAST(punch_in_time AS TIME) 
END AS shift_start_time,
CASE WHEN punch_out_time = '' 
  THEN NULL
ELSE 
  CAST(punch_out_time AS TIME) 
END AS shift_end_time,
CAST(punch_apply_date AS DATE) AS shift_date,
CASE 
  WHEN CAST(punch_in_time AS TIME) BETWEEN '6:00' AND '12:00' 
    THEN 'MORNING'
  WHEN CAST(punch_in_time AS TIME) BETWEEN '14:00' AND '17:00' 
    THEN 'AFTERNOON'
  WHEN CAST(punch_in_time AS TIME) BETWEEN '17:00' AND '19:00' 
    THEN 'EVENING'
  WHEN CAST(punch_in_time AS TIME) BETWEEN '19:00' AND '23:00' 
    THEN 'NIGHT'
END AS shift_type,
CAST(hours_worked AS FLOAT),
CASE WHEN paycode <> 'ABSENT'
  THEN 'P'
ELSE 'A'
END AS attendance,
CASE WHEN paycode = 'BREAK'
  THEN 'Y'
ELSE 'N'
END AS has_taken_break,
CASE WHEN paycode = 'BREAK'
  THEN CAST(hours_worked AS FLOAT)
ELSE 0
END AS break_hour,
CASE WHEN paycode = 'CHARGE'
  THEN 'Y'
ELSE 'N'
END AS was_charge,
CASE WHEN paycode = 'CHARGE'
  THEN CAST(hours_worked AS FLOAT)
ELSE 0
END AS charge_hour,
CASE WHEN paycode = 'ON_CALL'
  THEN 'Y'
ELSE 'N'
END AS was_on_call,
CASE WHEN paycode = 'ON_CALL'
  THEN CAST(hours_worked AS FLOAT)
ELSE 0
END AS on_call_hour
FROM raw_timesheet t
JOIN employee e
ON e.client_employee_id = t.employee_id;
