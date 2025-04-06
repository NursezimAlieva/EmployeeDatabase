import sqlite3
from datetime import datetime

class Employee:
    def __init__(self, id = None, name = '', position = '', salary = 0.0, hire_date = None):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.hire_date = hire_date if hire_date else datetime.now().strftime("%Y-%m-%d")

    def __str__(self):
        return f"Employee(id = {self.id}, name = '{self.name}', position = '{self.position}', salary = {self.salary}, hire_date = '{self.hire_date}')"

class EmployeeDAO:
    def __init__(self, db_name = "employee_db.sqlite"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS employee(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                position TEXT,
                                salary REAL,
                                hire_date TEXT)''')
        self.conn.commit()

    def insert(self, employee):
        self.cursor.execute("INSERT INTO employee (name, position, salary, hire_date) VALUES (?, ?, ?, ?)",
                            (employee.name, employee.position, employee.salary, employee.hire_date))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_by_id(self, id):
        self.cursor.execute("SELECT * FROM employee WHERE id = ?", (id,))
        row = self.cursor.fetchone()
        return  Employee(*row) if row else None

    def get_all(self):
        self.cursor.execute("SELECT * FROM employee")
        return [Employee(*row) for row in self.cursor.fetchall()]

    def update(self, employee):
        self.cursor.execute("UPDATE employee SET name = ?, position = ?, salary = ?, hire_date = ? WHERE id = ?",
                            (employee.name, employee.position, employee.salary, employee.hire_date, employee.id))
        self.conn.commit()

    def delete(self, id):
        self.cursor.execute("DELETE FROM employee WHERE id = ?", (id,))
        self.conn.commit()

    def close(self):
        self.conn.close()

if __name__ == "__main__":
    dao = EmployeeDAO()

    #Create
    new_employee = Employee(name = 'Nursezim Alieva', position = "Data Analyst", salary = 60000.0)
    new_employee.id = dao.insert(new_employee)
    print(f"Inserted: {new_employee}")

    #Read by ID
    retrieved = dao.get_by_id(new_employee.id)
    print(f"Retrieved: {retrieved}")

    #Read all
    all_employees = dao.get_all()
    print("All Employees:")
    for emp in all_employees:
        print(emp)

    #Update
    new_employee.position = "Senior Data Analyst"
    new_employee.salary = 90000.0
    dao.update(new_employee)
    print(f"Updated: {dao.get_by_id(new_employee.id)}")

    #Delete
    dao.delete(new_employee)
    print(f"Deleted Employee ID {new_employee.id}")

    dao.close