import unittest
from main import add


class Testmain(unittest.TestCase):
    def setUp(self):
        print('This function will run before each test cases')

    def test_case1(self):
        num1 = 10
        num2 = 20
        res = add(num1, num2)
        self.assertEqual(res, 30)

    def test_case_2(self):
        res = add('xyz', 2)
        # self.assertTrue(isinstance(res, ValueError))
        self.assertIsInstance(res, ValueError)

    def tearDown(self):
        print('This will run at the end of each test case')


if __name__ == '__main__':
    unittest.main()
