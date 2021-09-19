CREATE TABLE IF NOT EXISTS timesheet (
  timesheet_id SERIAL PRIMARY KEY,
  client_employee_id VARCHAR(255),
  client_department_id VARCHAR(255),
  shift_start_time TIME,
  shift_end_time TIME,
  shift_date DATE,
  shift_type VARCHAR(50),
  hours_worked FLOAT,
  attendance CHAR(1),
  has_taken_break CHAR(1),
  break_hour FLOAT,
  was_charge CHAR(1),
  charge_hour FLOAT,
  was_on_call CHAR(1),
  on_call_hour FLOAT, 
  CONSTRAINT fk_timesheet_employee_id
    FOREIGN KEY (client_employee_id)
    REFERENCES employee(client_employee_id)
    ON DELETE CASCADE,
  CONSTRAINT fk_timesheet_department_id
    FOREIGN KEY (client_department_id)
    REFERENCES department(client_department_id)
    ON DELETE CASCADE
);
