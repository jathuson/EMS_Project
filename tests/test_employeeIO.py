import unittest

from employeeIO import readEmployeesFile, writeNewEmployee, updateEmployee


class TestReadEmployeesFile(unittest.TestCase):
    def test_fields(self):
        employees = readEmployeesFile()
        employee = employees.popitem()
        required_fields = ['firstName', 'lastName', 'startDate', 'salary', 'department', 'empId']
        self.assertEqual(list(employee[1].keys()), required_fields)

    def test_dummy_employee(self):
        employees = readEmployeesFile()
        employee = employees.popitem()
        self.assertEqual(employee[1]['firstName'], 'John')
        self.assertEqual(employee[1]['lastName'], 'Doe')
        self.assertEqual(employee[1]['startDate'], '2020-01-01')
        self.assertEqual(employee[1]['salary'], '100000')
        self.assertEqual(employee[1]['department'], 'IT')
        self.assertEqual(employee[1]['empId'], '1'


class TestWriteNewEmployee(unittest.TestCase):
    def test_fields(self):
        pass


class TestUpdateEmployee(unittest.TestCase):
    def test_fields(self):
        pass


if __name__ == '__main__':
    unittest.main()