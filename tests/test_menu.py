import unittest
from unittest.mock import patch, MagicMock

from menu import remove_employee, list_employees
from employeeIO import readEmployeesFile, writeNewEmployee
from employee import Employee

class TestRemoveEmployee(unittest.TestCase):
    def setUp(self):
        # Create a new employee
        self.newEmployee = Employee("Test", "Case", "2020/12/24", 100000, "IL", 99)
        writeNewEmployee(self.newEmployee)


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


# class TestListEmployees(unittest.TestCase):
#     def test_list_employees_valid_id(self):
#         # Prepare the test data
#         test_id = "123"
#         employees = readEmployeesFile()

#         # Mock the input and print functions
#         with patch("builtins.input", return_value=test_id), patch("builtins.print") as mocked_print:
#             list_employees()

#             # Verify that the correct output is printed
#             employee = employees[test_id]
#             mocked_print.assert_any_call("Employee Information:")
#             mocked_print.assert_any_call(f"ID: {employee.emp_id}")
#             mocked_print.assert_any_call(
#                 f"Name: {employee.firstname} {employee.lastname}")
#             mocked_print.assert_any_call(f"Department: {employee.department}")
#             mocked_print.assert_any_call(
#                 f"Date of Employment: {employee.date_of_employment}")
#             mocked_print.assert_any_call(f"Salary: {employee.salary}")

#     def test_list_employees_invalid_id(self):
#         # Prepare the test data
#         test_id = "1"

#         # Mock the input and print functions
#         with patch("builtins.input", return_value=test_id), patch("builtins.print") as mocked_print:
#             list_employees()

#             # Verify that the correct output is printed
#             mocked_print.assert_called_once_with(
#                 f"Employee with ID {test_id} not found.")


if __name__ == "__main__":
    unittest.main()