from employeeDatabase import Employee
from employeeDatabase import EmployeeDAO

if __name__ == "__main__":
    dao = EmployeeDAO()

    new_employee = Employee(name='Nursezim Alieva', position="Data Analyst", salary=60000.0)
    new_employee.id = dao.insert(new_employee)
    print(f"Inserted: {new_employee}")

    retrieved = dao.get_by_id(new_employee.id)
    print(f"Retrieved: {retrieved}")

    all_employees = dao.get_all()
    print("All Employees:")
    for emp in all_employees:
        print(emp)

    new_employee.position = "Senior Data Analyst"
    new_employee.salary = 90000.0
    dao.update(new_employee)
    print(f"Updated: {dao.get_by_id(new_employee.id)}")

    dao.delete(new_employee)
    print(f"Deleted Employee ID {new_employee.id}")

