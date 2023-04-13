import unittest

from employeeIO import readEmployeesFile, writeNewEmployee, updateEmployee
import employee
import csv
from datetime import date


class TestReadEmployeesFile(unittest.TestCase):
    def test_fields(self):
        employees = readEmployeesFile()
        employee = employees.popitem()
        required_fields = ['firstName', 'lastName', 'startDate', 'salary', 'department', 'empId']
        self.assertEqual(list(employee[1].keys()), required_fields)

    def test_dummy_employee(self):
        employees = readEmployeesFile()
        writeNewEmployee(employee.Employee("John", "Doe", '2020-01-01', '100000', "IT", 1))
        employee = employees.popitem()
        self.assertEqual(employee[1]['firstName'], 'John')
        self.assertEqual(employee[1]['lastName'], 'Doe')
        self.assertEqual(employee[1]['startDate'], '2020-01-01')
        self.assertEqual(employee[1]['salary'], '100000')
        self.assertEqual(employee[1]['department'], 'IT')
        self.assertEqual(employee[1]['empId'], '1')


class TestWriteNewEmployee(unittest.TestCase):
    def test_fields(self):
        newEmployee = employee.Employee("Test", "Case", date.today(), 0, "WA", 0)
        csvFile = open("employees.csv", "w")
        fieldnames = ['firstName', 'lastName',
                      'startDate', 'salary', 'department', 'empId']
        write = csv.DictWriter(csvFile, fieldnames=fieldnames)
        write.writeheader()
        csvFile.close()

        writeNewEmployee(newEmployee)
        employees = readEmployeesFile()
        
        employeee = employees.popitem()
        requied_fields = ["Test", "Case", str(date.today()), str(0), "WA", str(1)]
        self.assertEqual(list(employeee[1].values()), requied_fields)



class TestUpdateEmployee(unittest.TestCase):
    def test_fields(self):
        newEmployee = employee.Employee("Test", "Case", date.today(), 1123, "WA", 0)
        csvFile = open("employees.csv", "w")
        fieldnames = ['firstName', 'lastName',
                      'startDate', 'salary', 'department', 'empId']
        write = csv.DictWriter(csvFile, fieldnames=fieldnames)
        write.writeheader()
        csvFile.close()

        writeNewEmployee(newEmployee)
        newEmployee._empId = 1
        writeNewEmployee(newEmployee)
        newEmployee._empId = 2
        writeNewEmployee(newEmployee)


        

        updatedEmployee = employee.Employee("Test", "Case", date.today(), 1000, "WA", 0)
        updateEmployee(updatedEmployee)
        employees = readEmployeesFile()
        
        employeee = employees.popitem()
        requied_fields = ["Test", "Case", str(date.today()), str(1000), "WA", str(1)]
        self.assertEqual(list(employeee[1].values()), requied_fields)


if __name__ == '__main__':
    unittest.main()