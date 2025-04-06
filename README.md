![Снимок экрана 2025-04-06 181541](https://github.com/user-attachments/assets/cd54edf2-55de-46cb-b9bc-4a728849b8a8)
# Employee Management System

This Python application allows for managing employee records using SQLite. It provides CRUD (Create, Read, Update, Delete) operations on an `employee` table.

## Features
- Insert new employees
- Retrieve employee by ID
- Retrieve all employees
- Update employee information
- Delete employee by ID

## Database Structure
Database: `employee_db.sqlite`

Table: `employee`
- `id` (INTEGER, Primary Key, Auto-increment)
- `name` (TEXT)
- `position` (TEXT)
- `salary` (REAL)
- `hire_date` (TEXT)

## Classes

### Employee
Represents an employee entity.

**Fields:**
- `id`: Unique identifier (int)
- `name`: Employee name (str)
- `position`: Job title (str)
- `salary`: Salary amount (float)
- `hire_date`: Date of hiring (str, format: YYYY-MM-DD)

**Methods:**
- `__init__()`: Initializes an employee object.
- `__str__()`: Returns a string representation of the employee.

### EmployeeDAO
Handles all database operations related to the `employee` table.

**Methods:**
- `__init__(db_name)`: Initializes the connection and creates the table if it doesn't exist.
- `create_table()`: Creates the employee table.
- `insert(employee)`: Inserts a new employee into the database.
- `get_by_id(id)`: Retrieves an employee by ID.
- `get_all()`: Retrieves all employees.
- `update(employee)`: Updates an existing employee.
- `delete(id)`: Deletes an employee by ID.
- `close()`: Closes the database connection.

## How to Run

1. **Install Python 3** if it's not already installed.
2. Save the main Python script (e.g., `employee_manager.py`).
3. Open your terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the script using the command:
   ```bash
   python employee_manager.py
   ```
6. Observe the printed output for insert, fetch, update, and delete operations.

## Notes
- The script creates the database file (`employee_db.sqlite`) in the same directory if it does not exist.
- The `hire_date` is set to the current date by default when a new `Employee` is created.
