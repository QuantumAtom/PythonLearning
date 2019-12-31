import unittest
from employee import Employees

class TestEmployees(unittest.TestCase):
    """Test for salary raises"""

    def setUp(self):
        """Generate a test subject for testing"""
        self.DLandingham = Employees('Delores','Landingham',40000)
    
    def test_give_default_raise(self):
        self.DLandingham.give_raise()
        self.assertEqual(self.DLandingham.Salary, 45000)

    def test_give_extra_raise(self, bigraise=6000):
        self.DLandingham.give_raise(bigraise)
        self.assertEqual(self.DLandingham.Salary, 46000)

unittest.main()
