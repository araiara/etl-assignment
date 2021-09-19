## Extraction
In this phase, the data are extracted from the given files of format CSV, JSON, and XML into our raw database. The databases raw_employee_data and raw_timesheet_data are populated.
  
### Considerations
- **Selection of the datatype**
  - The VARCHAR(500) datatype was given to all the attributes. Since we are extracting the data into our databases, the values of some of the data may not comply with the data types that are explicitly given. For example, the format of date in our data might not follow our standard DATE data type. Hence, all the data types were given as VARCHAR(500) with char limitation to 500, and further transformation will be done to convert all the VARCHAR(500) data types into their respective data types.
- **Execution of delete queries before every insertion query**
  - The raw database tables have no constraints that can uniquely define a record. The existing records can be inserted again if the program is executed. Hence, we execute delete queries before inserting new data to ensure the database has no records before insertion. 
 
- **Ignoring the first line from data**
  - The first line of the data file consists of the column headers. Hence, they are ignored while insertion.

### Pseudocode
- Select data file type.
- Connect to the database.
- Open CSV file in read mode | Load JSON | Parse XML as dictionary.
- For each record/line in the file
  - Prepare an insert query.
  - Execute the insert query.
- Close file.
- Commit connection.
- Close connection

## Extraction from DB

