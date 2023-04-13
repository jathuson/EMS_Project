import csv
from department import Department
from employee import Employee

FIELDNAMES = ["name", "budget", "phone"]


def readDepartmentCSV() -> dict:
    try:
        with open("departments.csv", "r") as csvFile:
            departments = {}
            [departments.update({line['name']: line}) for line in csv.DictReader(csvFile)]
    except FileNotFoundError:
        writeDepartmentHeader()
        return readDepartmentCSV()
    return departments


def writeNewDepartment(department: Department):
    try:
        with open("departments.csv", "a") as csvFile:
            write = csv.DictWriter(csvFile, fieldnames=FIELDNAMES)
            write.writerow(department.toDict())
    except FileNotFoundError:
        writeDepartmentHeader()
        writeNewDepartment(department)


def writeDepartmentHeader():
    with open("departments.csv", "w") as csvFile:
        write = csv.DictWriter(csvFile, fieldnames=FIELDNAMES)
        write.writeheader()


def updateDepartment():
    pass


def writeDepartmentCSV(departments):
    with open("departments.csv", "w") as csvFile:
        write = csv.DictWriter(csvFile, fieldnames=FIELDNAMES)
        write.writeheader()
        for _, department in departments:
            write.writerow(department.toDict())
