import unittest
import calculator

class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('SETUP class ********')

    @classmethod
    def tearDownClass(cls):
        print('TEAR DOWN class ********')

    def setUp(self):
        print('\nsetUp\n')
	
    def tearDown(self):
        print('\ntearDown\n')
		
    def test_add(self):
        #self.assertEqual(calculator.add(2,3), 6)
        print('test_Add===========')
        self.assertEqual(calculator.add(2,3), 5)
        #self.assertEqual(calculator.add(2,3), 4)

    def test_substract(self):
        print('test_substract===========')
        self.assertEqual(calculator.substract(3,1), 2)

    def test_divide(self):
        print('test_divide===========')
        self.assertEqual(calculator.divide(5,1), 5)
		
        self.assertRaises(ValueError, calculator.divide, 10, 0)
		
        #Context Manager
        with self.assertRaises(ValueError):
            calculator.divide(20,0)

    def test_multiply(self):
        print('test_multiply===========')
        self.assertEqual(calculator.multiply(5,1), 5)
	
     	
if __name__ == '__main__':
    unittest.main()
