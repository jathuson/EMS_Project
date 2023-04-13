import unittest

from employee import Employee


class TestEmployeeClass(unittest.TestCase):
    def test_dict_to_employee(self):
        employee = Employee.fromDict({"firstName": "John",
                                      "lastName": "Doe",
                                      "startDate": "2020-01-01",
                                      "salary": 100000,
                                      "department": "IT",
                                      "empId": 1})
        self.assertEqual(employee.firstname, "John")
        self.assertEqual(employee.lastname, "Doe")
        self.assertEqual(employee.startDate, "2020-01-01")
        self.assertEqual(employee.salary, 100000)
        self.assertEqual(employee.department, "IT")
        self.assertEqual(employee.empId, 1)