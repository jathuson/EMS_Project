import csv
class employee():
    first = "hi"
    last = "s"
    DOE = "DOE"
    salary = "sal"
    department = "dep"
    def __init__(self):
        first = "hi"
        last = "lasts"
        DOE = "DOE"
        salary = "sal"
        department = "dep"


def openEmployeeFile():
    try:
        csvFile = open("employees.csv", "a")
    except:
        csvFile = open("employees.csv", "w")
        fieldnames = ['first_name', 'last_name', 'DOE' , 'salary', 'department']
        write = csv.DictWriter(csvFile, fieldnames=fieldnames)
        write.writeheader()


    return csvFile

def closeEmployeeFile(csvFile):

    csvFile.close()

def writeNewEmployee(employee):

    file = openEmployeeFile()
    fieldnames = ['first_name', 'last_name', 'DOE' , 'salary', 'department']
    write = csv.DictWriter(file, fieldnames=fieldnames)
    write.writerow({'first_name' : employee.first, 'last_name': employee.last, 'DOE' : employee.DOE , 'salary': employee.salary, 'department': employee.department})
    closeEmployeeFile(file)



frank = employee()
writeNewEmployee(frank)

    