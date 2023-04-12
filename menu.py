# Imports from employee and department
from employee import Employee
from employeeWrite import writeNewEmployee
from file_read import readEmployeesCSV

def add_employee():
    firstname = input("Enter employee first name: ")
    lastname = input("Enter employee last name: ")
    emp_id = input("Enter employee id: ")
    date_of_employment = input("Enter employee date of employment: ")
    salary = input("Enter employee salary: ")
    department = input("Enter employee department: ")
    employee = Employee(firstname, lastname, date_of_employment, salary, department,emp_id) # calls on our employee class
    writeNewEmployee(employee) # write here
    print("Employee added successfully!")

def remove_employee():
    id = input("Enter employee id to remove: ")
    employees = readEmployeesCSV()
    for employee in employees:
        if employee.empId == id:
            employees.remove(employee)
            print("Employee removed successfully!")
            return
        else:
            print("Employee with id", id, "not found.")

def update_employee():
    id = input("Enter employee id to update: ")
    # Choose what information you want to change?
    fieldnames= ['firstname', 'lastname', 'id', 'date_of_employment','salary', 'department']
    #Go through each header in employee info and ask if they want to change this info or stay the same
    employees = readEmployeesCSV()
    for employee in employees:
        if employee.EmpId == id:
            for info in fieldnames:
            input_change= input(f'Do you want to change the {info}?(y/n)')
            if input_change.lower()=='y':
                    #Use employee class to update the information

    print("Employee with id", id, "not found.")

def list_employees():
    id=input('Enter the employee ID you wish to find: ')
    for employee in employees:
        if employee.id == id:
            print("Name:", employee.name, 
                "\nID:", employee.id, 
                "\nDate of Employment:", employee.date_of_employment, 
                "\nSalary:", employee.salary, 
                "\nDepartment:", employee.department)
        
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
        update_employee()
    elif choice == '4':
        list_employees()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")