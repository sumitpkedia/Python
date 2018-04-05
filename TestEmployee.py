

import unittest

from unittest.mock import patch

from Employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.emp_1 = Employee('John', 'Thomas', 500)
        self.emp_2 = Employee('Pankaj', 'laddha', 1000)

    def tearDown(self):
        pass

    def test_email(self):
        #self.assertEqual(self.emp_1.email, 'John.Thomas@email.com')
        self.assertEqual(self.emp_2.email, 'Pankaj.laddha@email.com')

    def test_fullname(self):
        #self.assertEqual(self.emp_1.fullname, 'John Thomas')
        self.assertEqual(self.emp_2.fullname, 'Pankaj laddha')

    def test_monthly_schedule(self):
        print('Test monthly schedule')
        with patch('Employee.requests.get') as mocked_get:
            mocked_get.return_vale.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Thomas/May')
            self.assertEqual(schedule, 'Success')


