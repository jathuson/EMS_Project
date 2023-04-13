import unittest
import datetime
from employee import Employee
from department import Department

class TestDepartment(unittest.TestCase):

    def setUp(self):
        self.dep1 = Department("Marketing", 10000, "123-456-7890")
        self.dep2 = Department("Sales", 15000, "098-765-4321")

        self.emp1 = Employee( "John", "Doe", datetime.date(2020, 1, 1), 50000, "Marketing", 0)
        self.emp2 = Employee( "Jane", "Smith", datetime.date(2021, 1, 1), 60000, "Sales", 1)
        self.emp3 = Employee( "Bob", "Johnson", datetime.date(2019, 1, 1), 55000, "Marketing", 2)
        self.emp4 = Employee( "Alice", "Williams", datetime.date(2022, 1, 1), 65000, "HR", 3)

        self.employeeDict1 = {
            0: self.emp1,
            1: self.emp2,
            2: self.emp3,
            3: self.emp4
        }

        self.employeeDict2 = {
            4: self.emp1,
            5: self.emp2,
            6: self.emp3,
            7: self.emp4
        }

    def test_inDep(self):
        expected_output = {1: self.emp1, 3: self.emp3}
        actual_output = self.dep1.inDep(self.employeeDict1)
        self.assertEqual(actual_output, expected_output)

    def test_fromDict(self):
        inpDict1 = {"name": "Marketing", "budget": 10000, "phone": "123-456-7890"}
        inpDict2 = {"name": "Sales", "budget": 15000, "phone": "098-765-4321"}
        # self.assertEqual(Department.fromDict(inpDict1), self.dep1)
        self.assertEqual(Department.fromDict(inpDict2), self.dep2)

    def test_name(self):
        self.assertEqual(self.dep1.name, "Marketing")
        self.dep1.name = "New Marketing"
        self.assertEqual(self.dep1.name, "New Marketing")

    def test_budget(self):
        self.assertEqual(self.dep2.budget, 15000)
        self.dep2.budget = 20000
        self.assertEqual(self.dep2.budget, 20000)

    def test_phone(self):
        self.assertEqual(self.dep1.phone, "123-456-7890")
        self.dep1.phone = "555-555-5555"
        self.assertEqual(self.dep1.phone, "555-555-5555")


if __name__ == '__main__':
    unittest.main()
