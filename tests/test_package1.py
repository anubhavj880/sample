import unittest

from package1 import action
from package1.subpackage1_1 import num


class TestPackag1(unittest.TestCase):
    a = 0
    b = 0

    def setUp(self):
        global a, b
        a = num.give_number()
        b = num.give_number()

    def test_add_integers(self):
        global a, b
        result = action.add(a, b)
        self.assertEqual(result, a + b)

    def test_minus_integers(self):
        global a, b
        result = action.minus(a, b)
        self.assertEqual(result, a - b)

    def tearDown(self):
        global a
        global b
        a = 0
        b = 0

if __name__ == '__main__':
    unittest.main()
