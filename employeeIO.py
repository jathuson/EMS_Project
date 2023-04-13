import csv
import shutil
from tempfile import NamedTemporaryFile

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
    fieldnames = ['firstName', 'lastName',
                  'startDate', 'salary', 'department', 'empId']
    write = csv.DictWriter(file, fieldnames=fieldnames)
    write.writerow(employee.toDict())
    closeEmployeeFile(file)



def updateEmployee(employee):
    
    tempFile = NamedTemporaryFile(mode="w", delete=False)
 
    fieldnames = ['firstName', 'lastName','startDate', 'salary', 'department', 'empId']
    
    filename ="employees.csv"

    with open(filename, 'r+') as file, tempFile:
        writer = csv.DictWriter(tempFile, fieldnames=fieldnames)
        reader = csv.DictReader(file, fieldnames=fieldnames)
        employee = employee.toDict()
        for row in reader:
            print(row)
            if row['empId'] == str(employee['empId']):
            
                row['firstName'] = employee['firstName']
                row['lastName'] = employee['lastName']
                row['startDate'] = employee['startDate']
                row['salary'] = employee['salary']
                row['department'] = employee['department']
                row['empId'] =  employee['empId']
                
            row = {'firstName': row['firstName'], 'lastName': row['lastName'], 'startDate': row['startDate'], 'salary': row['salary'], 'department': row['department'], 'empId': row['empId']}
            print("SLKDJNFSKDJFN")
            print(row)
            writer.writerow(row)
    shutil.move(tempFile.name, "employees.csv")
def removeEmployee(employee):
    
    tempFile = NamedTemporaryFile(mode="w", delete=False)
 
    fieldnames = ['firstName', 'lastName','startDate', 'salary', 'department', 'empId']
    
    filename ="employees.csv"

    with open(filename, 'r+') as file, tempFile:
        writer = csv.DictWriter(tempFile, fieldnames=fieldnames)
        reader = csv.DictReader(file, fieldnames=fieldnames)
        employee = employee.toDict()
        for row in reader:
            print(row)
            if row['empId'] != str(employee['empId']):
            
                               
                row = {'firstName': row['firstName'], 'lastName': row['lastName'], 'startDate': row['startDate'], 'salary': row['salary'], 'department': row['department'], 'empId': row['empId']}
                writer.writerow(row)
    shutil.move(tempFile.name, "employees.csv")
    


    

def removeEmployee(employee):
    tempFile = tempfile.NamedTemporryFile(mode="w", suffix=".py", prefix="employees")
 
    fieldnames = ['firstName', 'lastName','startDate', 'salary', 'department', 'empID']
    try:
        file = open("employees.csv", "r")
    except FileNotFoundError:
        file = open("employees.csv", "w")
        fieldnames = ['firstName', 'lastName',
                      'startDate', 'salary', 'department', 'empID']
        write = csv.DictWriter(file, fieldnames=fieldnames)
        write.writeheader()
    writer = csv.DictWriter(tempFile, fieldnames=fieldnames)
    reader = csv.DictReader(file, fieldnames=fieldnames)
    employee = employee.toDict()
    for row in reader:
        if row['empID'] != str(employee['empID']):
            row = {'firstName': row['firstName'], 'lastName': row['lastName'], 'startDate': row['startDate'], 'salary': row['salary'], 'department': row['department'], 'empID': row['empID']}
            writer.writerow(row)
    shutil.move(tempFile.name, "employees.csv")
    tempFile.close()
    file.close()

