import csv
import employee




def openEmployeeFile():
    try:
        csvFile = open("employees.csv", "a")
    except:
        csvFile = open("employees.csv", "w")
        fieldnames = ['firstname', 'lastname', 'startDate', 'salary', 'department', 'empID']
        write = csv.DictWriter(csvFile, fieldnames=fieldnames)
        write.writeheader()


    return csvFile

def closeEmployeeFile(csvFile):

    csvFile.close()

def writeNewEmployee(employee):

    file = openEmployeeFile()
    fieldnames = ['firstname', 'lastname', 'startDate', 'salary', 'department', 'empID']
    write = csv.DictWriter(file, fieldnames=fieldnames)
    write.writerow(employee.toDict)
    closeEmployeeFile(file)





    