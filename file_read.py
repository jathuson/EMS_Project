import json
import csv

# Read csv file as dictionary
def readEmployeesCSV():
    try:
        with open('employees.csv', 'r') as file:
            employees = [line for line in csv.DictReader(file)]
        return employees
    except FileNotFoundError:
        # If file not found, return empty dictionary
        return {}