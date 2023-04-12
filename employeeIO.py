import csv
import employee



    

  

def closeEmployeeFile(csvFile):

    csvFile.close()

# Read csv file as dictionary
def readEmployeesFile():
    try:
        csvFile = open("employees.csv", "r+")
    except FileNotFoundError:
        csvFile = open("employees.csv", "w")
        fieldnames = ['firstName', 'lastName',
                      'startDate', 'salary', 'department', 'empID']
        write = csv.DictWriter(csvFile, fieldnames=fieldnames)
        write.writeheader()
    employees = [line for line in csv.DictReader(file)]
    return employees

# Write new employee to csv file
def writeNewEmployee(employee):
    try:
        file = open("employees.csv", "a")
    except FileNotFoundError:
        file = open("employees.csv", "w")
        fieldnames = ['firstName', 'lastName',
                      'startDate', 'salary', 'department', 'empID']
        write = csv.DictWriter(file, fieldnames=fieldnames)
        write.writeheader()
    fieldnames = ['firstname', 'lastname',
                  'startDate', 'salary', 'department', 'empID']
    write = csv.DictWriter(file, fieldnames=fieldnames)
    write.writerow(employee.toDict)
    closeEmployeeFile(file)