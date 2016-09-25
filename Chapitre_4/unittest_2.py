#!/usr/bin/env python3
import unittest

class Operations:
    def __init__(self):
        pass

    def int_fois_deux(self, x):
        return int(x * 2)

    def int_fois_cinq(self, x):
        return int(x * 5)

class MyUnitTests(unittest.TestCase):
    def setUp(self):
        self.op = Operations()

    def testEquals(self):
        self.assertEqual(self.op.int_fois_deux(2), 4)
        self.assertEqual(self.op.int_fois_deux(6), 12)
        self.assertEqual(self.op.int_fois_cinq(5), 25)
        self.assertEqual(self.op.int_fois_cinq(10), 50)

    def testNotEquals(self):
        self.assertNotEqual(self.op.int_fois_deux(5), 1)
        self.assertNotEqual(self.op.int_fois_deux(15), 1)
        self.assertNotEqual(self.op.int_fois_cinq(12), 1)
        self.assertNotEqual(self.op.int_fois_cinq(52), 1)

    def testRaises(self):
        with self.assertRaises(ValueError):
            self.op.int_fois_deux('a')
        with self.assertRaises(ValueError):
            self.op.int_fois_deux('aa')

    def tearDown(self):
        del self.op

if __name__ == '__main__':
    unittest.main()
