#!/usr/bin/env python3

import unittest
from sortedArrays import elem

class Test_elem(unittest.TestCase):
    def test_oddLength(self):
        ls = [0,1,2]
        self.assertTrue(elem(0, ls))
        self.assertTrue(elem(1, ls))
        self.assertTrue(elem(2, ls))
        self.assertFalse(elem(-1, ls))
        self.assertFalse(elem(3, ls))

    def test_evenLenght(self):
        ls = [0,1]
        self.assertTrue(elem(0, ls))
        self.assertTrue(elem(1, ls))
        self.assertFalse(elem(2, ls))
        self.assertFalse(elem(-1, ls))

    def test_singleton(self):
        ls = [0]
        self.assertTrue(elem(0, ls))
        self.assertFalse(elem(1, ls))
        self.assertFalse(elem(-1, ls))

    def test_empty(self):
        ls = []
        self.assertFalse(elem(1, ls))
        self.assertFalse(elem(-1, ls))
        

# Run the tests
unittest.main()    
