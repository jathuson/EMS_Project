# Imports from employee and department
from employee import Employee
from employeeIO import writeNewEmployee, readEmployeesFile, updateEmployee
from inputUtility import *

departments = set()
def add_employee():
    firstname, lastname = getName()
    date_of_employment = getDate()
    salary = acceptInt("Please Enter the employee's salary: ", low=0, high=1_000_000_000)
    emp_id = acceptInt("Enter employee id: ", low=0, high=8_000_000_000)
    department = acceptStr("Enter employee department: ", departments)
    employee = Employee(firstname, lastname, date_of_employment, salary, department, emp_id) # calls on our employee class
    writeNewEmployee(employee) # write here
    print("Employee added successfully!")

def remove_employee():
    id = acceptInt("Enter the employee id that you want to remove: ", low = 0, high = 8_000_000_000)
    employees = readEmployeesFile()
    for employee in employees:
        if employee.empId == id:
            employees.remove(employee)
            print("Employee removed successfully!")
            return
        else:
            print("Employee with id", id, "not found.")

def get_changes_employee():
    while True:
        id = input("Enter employee id to update: ")
        employees = readEmployeesFile()
        if id not in employees:
            print("Invalid employee id, please try again.")
            continue
        print(employees[id])
        infocheck = input('Is this the correct info being displayed? (y/n)').lower()
        if infocheck == 'y':
            firstname, lastname = getName()
            date_of_employment = getDate()
            salary = acceptInt("Please Enter the employee's salary: ", low=0, high=1_000_000_000)
            department = acceptStr("Enter employee department: ", departments)
            employee = Employee(firstname, lastname, date_of_employment, salary, department, id)
            # Writes the new employee information into the employees.csv
            updateEmployee(employee)
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
    if id in employees:
        employee = employees[id]
        print("Employee Information:")
        print(f"ID: {employee.emp_id}")
        print(f"Name: {employee.firstname} {employee.lastname}")
        print(f"Department: {employee.department}")
        print(f"Date of Employment: {employee.date_of_employment}")
        print(f"Salary: {employee.salary}")
    else:
        print(f"Employee with ID {id} not found.")
        
# Welcome Message and main menu dialog, with choice for which task they would like to do.
def display_menu():
    print("Welcome to the Employee Management System!")
    print("1. Add employee")
    print("2. Remove employee")
    print("3. Update employee")
    print("4. List employees")
    print("5. Quit")


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