'''
This module provides a set of tests to run over a roman numeral converter
'''
from unittest import TestCase

from arabic2roman import ArabicRomanConverter

def test_arabic2roman():
    '''
    Order of test cases:
      1: Exact matches (simple)
        a: String data type
        b: Numerical data type
      2: Various inexact matches
        a: Round up
        b: Round down
      3: Invalid entries
        a: Less than 1 and decimals
        b: Numbers containing strings
      4: Edge cases that should succeed
        a: Currently focusing on whitespace in the input
    '''

    test_cases = ['5', '10', '50', '100', '500', '1000',        \
                   5,   10,   50,   100,   500,   1000,         \
                 '3', '17', '75', '249', '520', '1235',         \
                 '0', '-1', '1.2', '10000.2', '', '-10000',     \
                 'abc', 'a12', '/21', '_', '1241+', '-',        \
                 ' 1 ', '  5  ', '    5   ']

    truth_vals = ['V', 'X', 'L', 'C', 'D', 'M',                         \
                  'V', 'X', 'L', 'C', 'D', 'M',                         \
                 'III', 'XVII', 'LXXV', 'CCXLIX', 'DXX', 'MCCXXXV'] +   \
                 ['invalid input' for i in range(2*6)] +                \
                 ['I', 'V', 'V']

    results = []
    converter = ArabicRomanConverter('')
    for test_str in test_cases:
        result = converter.check_arabic(test_str)
        results.append(result)

    TestCase().assertListEqual(truth_vals, results)
