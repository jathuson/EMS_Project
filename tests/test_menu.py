import unittest
from unittest.mock import patch, MagicMock
import csv

from menu import remove_employee, list_employees, DEPARTMENTS
from employeeIO import readEmployeesFile, writeNewEmployee
from employee import Employee


# class TestAddEmployee(unittest.TestCase):
#     @patch("employeeIO.getName", return_value=("John", "Doe"))
#     @patch("employeeIO.getDate", return_value="2023-01-01")
#     @patch("employeeIO.acceptInt", side_effect=[50000, 123])
#     @patch("employeeIO.acceptStr", return_value="HR")
#     @patch("employeeIO.writeNewEmployee")
#     @patch("employeeIO.updateState")
#     @patch("builtins.print")
#     def test_add_employee(self, mocked_print, mocked_updateState, mocked_writeNewEmployee, mocked_acceptStr, mocked_acceptInt, mocked_getDate, mocked_getName):
#         # Call add_employee() with the mocks
#         add_employee()

#         # Verify getName(), getDate(), and acceptStr() were called
#         mocked_getName.assert_called_once()
#         mocked_getDate.assert_called_once()
#         mocked_acceptStr.assert_called_once_with(
#             "Enter employee department: ", set(DEPARTMENTS.keys()))

#         # Verify the Employee object is created with the correct data
#         mocked_writeNewEmployee.assert_called_once()
#         added_employee = mocked_writeNewEmployee.call_args[0][0]
#         self.assertIsInstance(added_employee, Employee)
#         self.assertEqual(added_employee.firstname, "John")
#         self.assertEqual(added_employee.lastname, "Doe")
#         self.assertEqual(added_employee.date_of_employment, "2023-01-01")
#         self.assertEqual(added_employee.salary, 50000)
#         self.assertEqual(added_employee.department, "HR")
#         self.assertEqual(added_employee.emp_id, 123)

#         # Verify updateState() and print() are called
#         mocked_updateState.assert_called_once()
#         mocked_print.assert_called_once_with("Employee added successfully!")


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
