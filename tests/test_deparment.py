import unittest
from department import Department
from employee import Employee


class TestDepartment(unittest.TestCase):

    def setUp(self):
        self.department = Department("Marketing", 10000, "123-456-7890")

    def test_init(self):
        self.assertEqual(self.department.name, "Marketing")
        self.assertEqual(self.department.budget, 10000)
        self.assertEqual(self.department.phone, "123-456-7890")

    def test_inDep(self):
        employeeDict = {
            1: Employee(1, "John", "Doe", "Marketing", 0, 1),
            2: Employee(2, "Jane", "Smith", "Sales", 0, 2),
            3: Employee(3, "Bob", "Johnson", "Marketing", 0, 3),
            4: Employee(4, "Alice", "Williams", "HR", 0, 4)
}
        expected = {
            1: Employee(1, "John", "Doe", "Marketing",  0, 1),
            3: Employee(3, "Bob", "Johnson", "Marketing", 0, 3)
        }
        self.assertEqual(self.department.inDep(employeeDict), expected)

    def test_fromDict(self):
        inpDict = {'name': 'Marketing', 'budget': 10000, 'phone': '123-456-7890'}
        expected = Department('Marketing', 10000, '123-456-7890')
        department = Department('Default', 0, '')
        self.assertEqual(department.fromDict(inpDict), expected)


if __name__ == '__main__':
    unittest.main()