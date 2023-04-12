import unittest

from employeeIO import readEmployeesFile, writeNewEmployee, updateEmployee


class TestReadEmployeesFile(unittest.TestCase):
    def test_fields(self):
        employees = readEmployeesFile()
        employee = employees.popitem()
        required_fields = ['firstName', 'lastName', 'startDate', 'salary', 'department', 'empId']
        self.assertEqual(list(employee[1].keys()), required_fields)


class TestWriteNewEmployee(unittest.TestCase):
    def test_fields(self):
        pass


class TestUpdateEmployee(unittest.TestCase):
    def test_fields(self):
        pass


if __name__ == '__main__':
    unittest.main()