import unittest
from backend_modules.numeric import *

class TestNumOperations(unittest.TestCase):

    def test_const_pi(self)
        self.assertAlmostEqual(const_pi(), 3.141592653589793, places=8)

    def test_atomic(self):
        self.assertEqual(atomic('5'), 5)
        self.assertEqual(atomic('-7'), -7)
    
    def test_binary_op(self):
        self.assertEqual(binary_op('+', 2, 3), 5)
        self.assertEqual(binary_op('-', 7, 4), 3)

if __name__ == '__main__':
    unittest.main()