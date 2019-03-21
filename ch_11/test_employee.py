import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """Creates an Employee for Testing"""
        self.employee = Employee('Pam', 'Beesly', 30000)

    def test_give_default_raise(self):
        """Test that an employee can be given a default raise"""
        old_salary = self.employee.annual_salary
        new_salary = self.employee.give_raise()
        self.assertEqual(new_salary - old_salary, 5000)

    def test_give_custom_raise(self):
        """Test that an employee can be give a custom raise"""
        old_salary = self.employee.annual_salary
        new_salary = self.employee.give_raise(8000)
        self.assertEqual(new_salary - old_salary, 8000)

unittest.main()