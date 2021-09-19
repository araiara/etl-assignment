CREATE TABLE IF NOT EXISTS fact_timesheet (
  id SERIAL PRIMARY KEY,
  employee_id INT,
  work_date DATE,
  department_id INT,
  hours_worked FLOAT,
  shift_type_id INT,
  punch_in_time TIME,
  punch_out_time TIME,
  attendance CHAR(1),
  has_taken_break CHAR(1),
  break_hour FLOAT,
  was_charge CHAR(1),
  charge_hour FLOAT,
  was_on_call CHAR(1),
  on_call_hour FLOAT,
  is_weekend CHAR(1),
  CONSTRAINT fk_fact_timesheet_employee_id
    FOREIGN KEY (employee_id)
      REFERENCES fact_employee(id),
  CONSTRAINT fk_fact_timesheet_department_id
    FOREIGN KEY (department_id)
      REFERENCES dim_department(id),
  CONSTRAINT fk_fact_timesheet_shift_type_id
    FOREIGN KEY (shift_type_id)
      REFERENCES dim_shift_type(id)
);
