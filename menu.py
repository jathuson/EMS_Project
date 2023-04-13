# Imports from employee and department
from employee import Employee
from employeeIO import writeNewEmployee, readEmployeesFile, updateEmployee, removeEmployee
from inputUtility import *
from department import Department
from departmentIO import readDepartmentCSV, updateDepartment, writeNewDepartment, writeDepartmentCSV

DEPARTMENTS = readDepartmentCSV()
EMPLOYEES = readEmployeesFile()


def add_employee():
    firstname, lastname = getName()
    date_of_employment = getDate()
    salary = acceptInt("Please Enter the employee's salary: ", low=0, high=1_000_000_000)    
    
    try:
        lastEMP = EMPLOYEES.popitem()
        emp_id =lastEMP[1]['empId']
    except:
       
        emp_id = 0
    

    department = acceptStr("Enter employee department: ", set(DEPARTMENTS.keys()))
    employee = Employee(firstname, lastname, date_of_employment, salary, department, emp_id) # calls on our employee class
    writeNewEmployee(employee) # write here
    updateState()
    print("Employee added successfully!")


def remove_employee():
    id = acceptInt("Enter the employee id that you want to remove: ", low = 0, high = 8_000_000_000)
    updateState()
    employees = EMPLOYEES.copy()

    for employee in employees:
        if employees[employee]['empId'] == str(id):
            employee_object = Employee.fromDict(employees[employee])
            del employees[employee]
            removeEmployee(employee_object)
            print("Employee removed successfully!")
            return
        else:
            print("Employee with id", id, "not found.")


def get_changes_employee():
    while True:
        id = input("Enter employee id to update: ")
        employees = EMPLOYEES.copy()
        if id not in employees:
            print("Invalid employee id, please try again.")
            continue

        print("Employee Information:")
        print(f"ID: {employee.emp_id}")
        print(f"Name: {employee.firstname} {employee.lastname}")
        print(f"Department: {employee.department}")
        print(f"Date of Employment: {employee.date_of_employment}")
        print(f"Salary: {employee.salary}")
        
        infocheck = input('Is this the correct info being displayed? (y/n)').lower()
        if infocheck == 'y':
            firstname, lastname = getName()
            date_of_employment = getDate()
            salary = acceptInt("Please Enter the employee's salary: ", low=0, high=1_000_000_000)
            department = acceptStr("Enter employee department: ", set(DEPARTMENTS.keys()))
            employee = Employee(firstname, lastname, date_of_employment, salary, department, id)
            # Writes the new employee information into the employees.csv
            updateEmployee(employee)
            updateState()
            break
        elif infocheck == 'n':
            continue
        else:
            print("Invalid input, please try again.")
            continue
    
def list_employees():
    id = input("Enter employee id to list information: ")
    # Show employee information
    employees = readEmployeesFile()
    try:
        if id in employees.keys():
            employee = employees[id]
            print("Employee Information:")
            print(f"ID: {employee['empId']}")
            print(f"Name: {employee['firstName']} {employee['lastName']}")
            print(f"Department: {employee['department']}")
            print(f"Date of Employment: {employee['startDate']}")
            print(f"Salary: {employee['salary']}")
        else:
            print(f"Employee with ID {id} not found.")
    except KeyError:
        print(f"Employee with ID {id} not found.")

def add_department():
    name = input("Please enter the name of the new department: \n")
    budget = acceptInt("Please enter the departments budget: ", 0, 1_000_000_000_000)
    phone = getPhone()
    department = Department(name, budget, phone)
    writeNewDepartment(department)
    updateState()


def remove_department():
    name = input("Please enter the name of the department you wish to delete: \n")
    departments: dict = readDepartmentCSV()
    if name in departments.keys():
        departments.pop(name)
        writeDepartmentCSV(departments)
        updateState()
    else:
        print(f"Error: Department {name} not found")


def update_department():
    while True:
        name = input("Enter name of department you wish to edit:\n")
        departments = DEPARTMENTS.copy()
        if name not in departments.keys():
            print(f"Cannot find {name} in departments")
            continue
        print(departments[name])
        infocheck = input('Is this the correct info being displayed? (y/n)').lower()
        if infocheck == 'y':
            name = input("Please enter the new department name:\n")
            budget = acceptInt("Please Enter the departments budget: ", low=0, high=10_000_000_000_000)
            phone = acceptStr("Enter employee department: ", set(DEPARTMENTS.keys()))
            department = Department(name, budget, phone)
            writeDepartmentCSV(departments)
            updateState()
            break
        elif infocheck == 'n':
            continue
        else:
            print("Invalid input, please try again.")
            continue
    print("Department Successfully updated")


def list_departments():
    departments = readDepartmentCSV()
    for department in departments:
        print(department)


def list_employees_by_department():
    name = input("Please enter the name of the department you wish to see: \n")
    departments = readDepartmentCSV()
    employees = readEmployeesFile()
    if name in departments.keys():
        department = departments[name]
        print(department)
        employeesInDep = department.inDep(employees)
        for _, employee in employeesInDep:
            print(employee)
        return True
    else:
        print(f"Error: Department {name} not found")
        return False
        
# Welcome Message and main menu dialog, with choice for which task they would like to do.
def display_menu():
    print("Welcome to the Employee Management System!")
    print("1. Add employee")
    print("2. Remove employee")
    print("3. Update employee")
    print("4. List employees")
    print("5. Quit")


def updateState():
    global DEPARTMENTS
    DEPARTMENTS = readDepartmentCSV()
    global EMPLOYEES
    EMPLOYEES = readEmployeesFile()


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            add_employee()
        elif choice == '2':
            remove_employee()
        elif choice == '3':
            get_changes_employee()
        elif choice == '4':
            list_employees()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
