INSERT INTO fact_timesheet (
  employee_id, work_date, department_id, hours_worked, shift_type_id, punch_in_time, punch_out_time, attendance, has_taken_break, break_hour, was_charge, charge_hour, was_on_call, on_call_hour, is_weekend
)
SELECT
  e.id,
  t.shift_date,
  d.id,
  t.hours_worked,
  s.id,
  t.shift_start_time,
  t.shift_end_time,
  t.attendance,
  t.has_taken_break,
  t.break_hour,
  t.was_charge,
  t.charge_hour,
  t.was_on_call,
  t.on_call_hour,
  CASE WHEN EXTRACT(DOW FROM t.shift_date) = 0 
  OR EXTRACT(DOW FROM t.shift_date) = 6
    THEN 'Y'
  ELSE 'N' 
  END
FROM timesheet t
JOIN fact_employee e 
  ON t.client_employee_id = e.client_employee_id
JOIN dim_shift_type s 
  ON t.shift_type = s.shift_name
JOIN dim_department d 
  ON t.client_department_id = d.client_department_id;