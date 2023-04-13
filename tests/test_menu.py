import unittest
from unittest.mock import patch, MagicMock
import csv

from menu import remove_employee, list_employees, DEPARTMENTS, add_employee
from employeeIO import readEmployeesFile, writeNewEmployee
from employee import Employee


class TestAddEmployee(unittest.TestCase):
    def setUp(self):
        # Create a new employee
        self.newEmployee = Employee(
            "John", "Doe", "2020/12/24", 100000, "IL", 500)
        writeNewEmployee(self.newEmployee)

    # delete everything after the first line in employees.csv after each test to ensure that the test is independent
    def tearDown(self):
        with open("employees.csv", "w") as csvFile:
            fieldnames = ['firstName', 'lastName',
                          'startDate', 'salary', 'department', 'empId']
            write = csv.DictWriter(csvFile, fieldnames=fieldnames)
            write.writeheader()

    @patch('builtins.input', create=True)
    def test_add_employee(self, mocked_input):
        mocked_input.side_effect = ['John Doe', "2023 01 01", '50005', 'HR']

        # Call add_employee() with the mocks
        add_employee()

        mocked_input.assert_called_with("Employee added successfully!")


class TestRemoveEmployee(unittest.TestCase):
    def setUp(self):
        # Create a new employee
        self.newEmployee = Employee(
            "Test", "Case", "2020/12/24", 100000, "IL", 99)
        writeNewEmployee(self.newEmployee)

    # delete everything after the first line in employees.csv after each test to ensure that the test is independent
    def tearDown(self):
        with open("employees.csv", "w") as csvFile:
            fieldnames = ['firstName', 'lastName',
                          'startDate', 'salary', 'department', 'empId']
            write = csv.DictWriter(csvFile, fieldnames=fieldnames)
            write.writeheader()

    @patch("builtins.print")
    def test_remove_employee(self, mocked_print):
        # Prepare the test data
        test_id = '100'

        with patch("builtins.input", return_value=test_id), patch("builtins.print") as mocked_print:
            # Call remove_employee() with the mocks
            remove_employee()

            # Verify the employee is removed
            self.assertNotIn("100", readEmployeesFile())

            # Verify the success message is printed
            mocked_print.assert_called_with("Employee removed successfully!")


class TestListEmployees(unittest.TestCase):
    def setUp(self):
        # Create a new employee
        self.newEmployee = Employee(
            "Test", "Case", "2020/12/24", 100000, "IL", 99)
        writeNewEmployee(self.newEmployee)

    # delete everything after the first line in employees.csv after each test to ensure that the test is independent
    def tearDown(self):
        with open("employees.csv", "w") as csvFile:
            fieldnames = ['firstName', 'lastName',
                          'startDate', 'salary', 'department', 'empId']
            write = csv.DictWriter(csvFile, fieldnames=fieldnames)
            write.writeheader()

    def test_list_employees_valid_id(self):
        # Prepare the test data
        test_id = "100"
        employees = readEmployeesFile()

        # Mock the input and print functions
        with patch("builtins.input", return_value=test_id), patch("builtins.print") as mocked_print:
            list_employees()

            # Verify that the correct output is printed
            employee = employees[test_id]
            mocked_print.assert_any_call("Employee Information:")
            mocked_print.assert_any_call(f"ID: {employee['empId']}")
            mocked_print.assert_any_call(
                f"Name: {employee['firstName']} {employee['lastName']}")
            mocked_print.assert_any_call(
                f"Department: {employee['department']}")
            mocked_print.assert_any_call(
                f"Date of Employment: {employee['startDate']}")
            mocked_print.assert_any_call(f"Salary: {employee['salary']}")

    def test_list_employees_invalid_id(self):
        # Prepare the test data
        test_id = "123456789"

        # Mock the input and print functions
        with patch("builtins.input", return_value=test_id), patch("builtins.print") as mocked_print:
            list_employees()

            # Verify that the correct output is printed
            mocked_print.assert_called_once_with(
                f"Employee with ID {test_id} not found.")


if __name__ == "__main__":
    unittest.main()
