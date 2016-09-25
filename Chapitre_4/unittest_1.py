#!/usr/bin/env python3
import unittest

def int_fois_deux(x):
    return int(x * 2)

def int_fois_cinq(x):
    return int(x * 5)

class MyUnitTests(unittest.TestCase):
    @unittest.skip('non fonctionel')
    def testEquals(self):
        self.assertEqual(int_fois_deux(2), 4)
        self.assertEqual(int_fois_deux(6), 12)
        self.assertEqual(int_fois_cinq(5), 25)
        self.assertEqual(int_fois_cinq(10), 50)
        self.assertEqual(int_fois_deux(10), 50)

    def testNotEquals(self):
        self.assertNotEqual(int_fois_deux(5), 1)
        self.assertNotEqual(int_fois_deux(15), 1)
        self.assertNotEqual(int_fois_cinq(12), 1)
        self.assertNotEqual(int_fois_cinq(52), 1)

    def testRaises(self):
        with self.assertRaises(ValueError):
            int_fois_deux('a')
        with self.assertRaises(ValueError):
            int_fois_deux('aa')

if __name__ == '__main__':
    unittest.main()
