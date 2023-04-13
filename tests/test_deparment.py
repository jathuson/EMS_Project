import unittest
from department import Department
from employee import Employee

class TestDepartment(unittest.TestCase):
    def setUp(self):
        self.department = Department("Marketing", 1000000, "555-1234")

    def test_name(self):
        self.assertEqual(self.department.name, "Marketing")
        
   
    
        
if __name__ == '__main__':
    unittest.main()