import json
import csv

# Read csv file as dictionary
def readEmployeesCSV():
    with open('employees.csv', 'r') as file:
        employees = [line for line in csv.DictReader(file)]
    return employees
