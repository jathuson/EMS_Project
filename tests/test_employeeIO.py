import unittest
import csv
from datetime import date

from employeeIO import readEmployeesFile, writeNewEmployee, updateEmployee, removeEmployee
from employee import Employee


class TestReadEmployeesFile(unittest.TestCase):
    def setUp(self):
        # Create a new employee
        self.newEmployee = Employee(
            "John", "Doe", '2020-01-01', '100000', "IT", 55)
        writeNewEmployee(self.newEmployee)

    def test_fields(self):
        employees = readEmployeesFile()
        employee = employees.popitem()
        required_fields = ['firstName', 'lastName', 'startDate', 'salary', 'department', 'empId']
        self.assertEqual(list(employee[1].keys()), required_fields)

    def test_dummy_employee(self):
        employees = readEmployeesFile()
        
        employee = employees['56']
        self.assertEqual(employee['firstName'], 'John')
        self.assertEqual(employee['lastName'], 'Doe')
        self.assertEqual(employee['startDate'], '2020-01-01')
        self.assertEqual(employee['salary'], '100000')
        self.assertEqual(employee['department'], 'IT')
        self.assertEqual(employee['empId'], '56')


class TestWriteNewEmployee(unittest.TestCase):
    def test_fields(self):
        newEmployee = Employee("Test", "Case", date.today(), 0, "WA", 0)
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
        newEmployee = Employee("Test", "Case", date.today(), 1123, "WA", 0)
        csvFile = open("employees.csv", "w")
        fieldnames = ['firstName', 'lastName',
                      'startDate', 'salary', 'department', 'empId']
        write = csv.DictWriter(csvFile, fieldnames=fieldnames)
        write.writeheader()
        csvFile.close()

        writeNewEmployee(newEmployee)

        updatedEmployee = Employee("Test", "Case", date.today(), 1000, "WA", 0)
        updateEmployee(updatedEmployee)
        employees = readEmployeesFile()
        
        employeee = employees.popitem()
        requied_fields = ["Test", "Case", str(date.today()), str(1000), "WA", str(1)]
        self.assertEqual(list(employeee[1].values()), requied_fields)


class TestRemoveEmployee(unittest.TestCase):
    def test_fields(self):
        newEmployee = Employee("Test", "Case", date.today(), 1123, "WA", 0)
        csvFile = open("employees.csv", "w")
        fieldnames = ['firstName', 'lastName',
                      'startDate', 'salary', 'department', 'empId']
        write = csv.DictWriter(csvFile, fieldnames=fieldnames)
        write.writeheader()
        csvFile.close()

        writeNewEmployee(newEmployee)

        newEmployee = Employee("Test", "Case", date.today(), 1, "WA", 1)
        writeNewEmployee(newEmployee)        

        removedEmployee = Employee("Test", "Case", date.today(), 1000, "WA", 0)
        removeEmployee(removedEmployee)
        employees = readEmployeesFile()
        
        employeee = employees.popitem()
        
        requied_fields = ["Test", "Case", str(date.today()), str(1), "WA", str(2)]
        self.assertEqual(list(employeee[1].values()), requied_fields)


if __name__ == '__main__':
    unittest.main()