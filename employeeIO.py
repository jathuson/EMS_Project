import csv
import shutil
import tempfile

def closeEmployeeFile(csvFile):

    csvFile.close()

# Read csv file as dictionary
def readEmployeesFile() -> dict:
    try:
        csvFile = open("employees.csv", "r")
    except FileNotFoundError:
        csvFile = open("employees.csv", "w")
        fieldnames = ['firstName', 'lastName',
                      'startDate', 'salary', 'department', 'empId']
        write = csv.DictWriter(csvFile, fieldnames=fieldnames)
        write.writeheader()
    employees = {}
    [employees.update({line['empId']: line}) for line in csv.DictReader(csvFile)] # Load employees into dictionary
    closeEmployeeFile(csvFile)
    return employees

# Write new employee to csv file
def writeNewEmployee(employee):
    try:
        file = open("employees.csv", "a")
    except FileNotFoundError:
        file = open("employees.csv", "w")
        fieldnames = ['firstName', 'lastName',
                      'startDate', 'salary', 'department', 'empId']
        write = csv.DictWriter(file, fieldnames=fieldnames)
        write.writeheader()
    fieldnames = ['firstname', 'lastname',
                  'startDate', 'salary', 'department', 'empId']
    write = csv.DictWriter(file, fieldnames=fieldnames)
    write.writerow(employee.toDict())
    closeEmployeeFile(file)



def updateEmployee(employee):
    
    tempFile = tempfile.NamedTemporryFile(mode="w", suffix=".py", prefix="employees")
 
    fieldnames = ['firstName', 'lastName','startDate', 'salary', 'department', 'empId']
    try:
        file = open("employees.csv", "r")
    except FileNotFoundError:
        file = open("employees.csv", "w")
        fieldnames = ['firstName', 'lastName',
                      'startDate', 'salary', 'department', 'empId']
        write = csv.DictWriter(file, fieldnames=fieldnames)
        write.writeheader()
    writer = csv.DictWriter(tempFile, fieldnames=fieldnames)
    reader = csv.DictReader(file, fieldnames=fieldnames)
    employee = employee.toDict()
    for row in reader:
        if row['empId'] == str(employee['empId']):
            row['firstName'], row['lastName'], row['startDate'], row['salary'], row['department'], row['empId'] =  employee['firstName'], employee['lastName'], employee['startDate'], employee['salary'], employee['department'], employee['empId']
        row = {'firstName': row['firstName'], 'lastName': row['lastName'], 'startDate': row['startDate'], 'salary': row['salary'], 'department': row['department'], 'empId': row['empId']}
        writer.writerow(row)
    shutil.move(tempFile.name, "employees.csv")
    tempFile.close()
    file.close()


