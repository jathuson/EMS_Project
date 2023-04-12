# Imports from employee and department

employees = []
def add_employee():
    firstname = input("Enter employee first name: ")
    lastname = input("Enter employee last name: ")
    id = input("Enter employee id: ")
    date_of_employment = input("Enter employee date of employment: ")
    salary = input("Enter employee salary: ")
    department = input("Enter employee department: ")
    employee = Employee(firstname, lastname, id, date_of_employment, salary, department) # calls on our employee class
    employees.append(employee) # write here
    print("Employee added successfully!")

def remove_employee():
    id = input("Enter employee id to remove: ")
    for employee in employees:
        if employee.id == id:
            employees.remove(employee)
            print("Employee removed successfully!")
            return
        else:
            print("Employee with id", id, "not found.")

def update_employee():
    id = input("Enter employee id to update: ")
    # Choose what information you want to change?
    employee_info = ['firstname', 'lastname', 'id', 'date_of_employment','salary', 'department']
    #Go through each header in employee info and ask if they want to change this info or stay the same
    for info in employee_info:
        input_change= input(f'Do you want to change the {info}?(y/n)')
        if input_change.lower()=='y':
            for employee in employees:
                if employee.id == id:
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