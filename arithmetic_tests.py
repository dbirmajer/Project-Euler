#!/usr/bin/env python3

import unittest
from arithmetic import q

class TestSmallestDivisor(unittest.TestCase):
    def test_one(self):
        self.assertEqual(q(12),  2)
        self.assertEqual(q(100),  2)
        self.assertEqual(q(9), 3)
        self.assertEqual(q(16), 2)
    def test_primes(self):
        self.assertEqual(q(5), 5)
        self.assertEqual(q(11), 11)

    # def test_one_find(self):
    #     self.assertEqual(is_valid_IP_find('12.255.56.1'), True)

    # def test_two_find(self):
    #     self.assertEqual(is_valid_IP_find(''),                False)
    #     self.assertEqual(is_valid_IP_find('abc.def.ghi.jkl'), False)
    #     self.assertEqual(is_valid_IP_find('123.456.789.0'),   False)
    #     self.assertEqual(is_valid_IP_find('12.34.56'),        False)
    #     self.assertEqual(is_valid_IP_find('12.34.56 .1'),     False)
    #     self.assertEqual(is_valid_IP_find('12.34.56.-1'),     False)
    #     self.assertEqual(is_valid_IP_find('123.045.067.089'), False)
    #     self.assertEqual(is_valid_IP_find('127.1.1.0'),        True)
    #     self.assertEqual(is_valid_IP_find('0.0.0.0'),          True)
    #     self.assertEqual(is_valid_IP_find('0.34.82.53'),       True)
    #     self.assertEqual(is_valid_IP_find('192.168.1.300'),   False)

    # def test_three_find(self):
    #     self.assertEqual(is_valid_IP_find('0.34.08.53'),       False)
        
    #     # def test_four(self):        
    # #     self.assertEqual(is_valid_IP_bp('0.34.02.53'),       False)

# Run the tests
unittest.main()    
