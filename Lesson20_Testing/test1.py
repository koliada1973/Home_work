import unittest
import My_functions_for_tests

class Full_Name_Test_Case(unittest.TestCase):
    def test_full_name(self):
        full = My_functions_for_tests.full_name('carl', 'johnson')
        full2 = My_functions_for_tests.full_name('cARL', 'jOHNSON')
        self.assertEqual(full, 'Carl Johnson')
        self.assertEqual(full2, 'Carl Johnson')

if __name__ == '__main__':
    unittest.main()
