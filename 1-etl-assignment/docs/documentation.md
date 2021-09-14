# Logical Modeling for Employee Timesheet

The following is the logical modeling of the data warehouse for employee timesheet management.

## Business Requirements
The following are the identified business requirements:
- The identified domain is health care.
- Gain insights into the workload of the employees.
- Information about the employee and their work schedules are required.
- Analyze the data in terms of their role, departments they work at, working shift, and so on.

## Data Modeling
### 1. Identifying subject areas
The following are the identified subject areas:
- employee
- department
- timesheet

### 2. Identifying dimensions
The following are the identified dimensions:
- **employee** - provides information about the employees such as their name, hire date, termination date, and so on.
- **department** - provides information about the department name.
- **time** - provides information about the date that has been granularized into the year, month, and day; punch in and out times, and so on. 
- **status** - provides information about the working status as working, on break, on-call, and so on.
- **shift** - provides information about the working shift such as morning or afternoon according to the time slots.
- **role** - provides information about the work role.

### 3. Identifying facts
The facts that were identified are the salary of the employee, their total working hours, and their fte. Hence, a fact table employee_timesheet is introduced that measures the dimensions.

### 4. Identifying required attributes and relationships between the fact and dimension tables
The following are the identified attributes for the dimension and fact tables.
Table Name              | Attributes
----------------------- | ----------------------------------------------------------------------------------------------------------------------------------
employee_dimension      | employee_id, first_name, last_name, manager_employee_id, hire_date, terminated_date, terminated_reason, dob, location, cost_center
department_dimension    | department_id, department_name
time_dimension          | time_id, year, month, day, week, week_day, punch_in_time, punch_out_time)
status_dimension        | status_id, pay_code
shift_dimension         | shift_id, shift_name, start_time, end_time
role_dimension          | role_id, employee_role
employee_timesheet_fact | employee_id, department_id, role_id,  shift_id, time_id, status_id, salary, fte, hours_worked

Here, the dimension keys are given as employee_id, department_id, role_id, shift_id, time_id, and status_id that measures the salary, fte, and working hours of the employees.

## Logical Model
![](1-etl-assignment/docs/logical-model.png)


[Link to the diagram]
(https://app.diagrams.net/#G1cd0tsSuuvPbDWV3TOya3-cSMi2u3s3xS)