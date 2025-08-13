import unittest
from class_for_test import Mathematician

class Test_Mathematician(unittest.TestCase):
    def setUp(self):
        self.m = Mathematician()

    def test_square_nums(self):
        self.assertEqual(self.m.square_nums([7, 11, 5, 4]), [49, 121, 25, 16])

    def test_remove_positives(self):
        self.assertEqual(self.m.remove_positives([0, 26, -11, -8, 13, -90]), [0, -11, -8, -90])

    def test_filter_leaps(self):
        self.assertEqual(self.m.filter_leaps([1600, 1700, 1800, 1900, 2000, 2005, 2011, 2020, 2021, 2024]), [1600, 2000, 2020, 2024])

if __name__ == '__main__':
    unittest.main()