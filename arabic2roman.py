#!/usr/bin/env python
'''
Convert an arabic number to a roman numeral
'''

from sys import stderr

class ArabicRomanConverter:
    '''
    Container to convert an arabic number to a roman numeral
    '''
    arab_string = str()
    arab_num = int()
    roman_string = str()
    def check_arabic(self, arabic_str):
        '''
        This is the first of a waterfall of functions

        This checks if an input is valid.
        -- If valid, calls the next function to convert the roman numeral
        -- If invalid, returns an error string prints debug info to stderr
        '''
        try:
            # First make a float so we can compare it to an int later
            num = float(arabic_str)

        except ValueError:
            if len(arabic_str) == 0:
                print(f'Invalid input -- no input provided', file = stderr)
                return 'invalid input'

            print(f'Invalid input ({arabic_str}) -- cannot make double', file=stderr)
            return 'invalid input'


        if int(num) != num:
            print(f'Invalid input ({arabic_str}) -- contains fraction', file=stderr)
            return 'invalid input'
        if num < 1:
            print(f'Invalid input ({arabic_str}) -- less than zero', file=stderr)
            return 'invalid input'

        # Define class variables
        self.arab_string = arabic_str
        self.arab_num = num
        return self.arabic2roman()

    def arabic2roman(self):
        '''
        This function converts an arabic number (as a string) into a roman numeral

        Error checking is performed in a different method,
        this function assumes the input is already valid

        We also need to define subtraction rules, using "Dr. Maths" rules:
          1. Subtract only powers of 10 (I, X, C)
          2. Subtract only a single letter
          3. Do not differ by more than an order of magnitude
        This yields a few more options:
        IV: 4
        IX: 9
        XL: 40
        XC: 90
        CD: 400
        CM: 900
        '''
        num = self.arab_num

        roman_string = []
        num_map = {1: 'I',  \
                   4: 'IV', \
                   5: 'V',  \
                   9: 'IX', \
                  10: 'X',  \
                  40: 'XL', \
                  50: 'L',  \
                  90: 'XC', \
                 100: 'C',  \
                 400: 'CD', \
                 500: 'D',  \
                 900: 'CM', \
                1000: 'M'}
        test_nums = list(num_map.keys())
        test_nums.sort()
        while num > 0:
            roman2add = max([romans for romans in test_nums if num >= romans])
            roman_string.append(num_map[roman2add])
            num = num - roman2add
        # def nextAdd(num):
        #     roman2add = max([romans for romans in testNums if num >= romans])
        #     romanString.append(num_map[roman2add])
        #     num = num - roman2add
        # def nextSubtr(num):
        self.roman_string = roman_string
        return ''.join(roman_string)

    def test_arabic2roman(self):
        '''
        Order of test cases:
          1: Exact matches
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
                     '3', '17', '75', '249', '520', '1235',         \
                     '0', '-1', '1.2', '10000.2', '', '-10000',     \
                     'abc', 'a12', '/21', '_', '1241+', '-',        \
                     ' 1 ', '  5  ', '    5   ']

        truth_vals = ['V', 'X', 'L', 'C', 'D', 'M',                         \
                     'III', 'XVII', 'LXXV', 'CCXLIX', 'DXX', 'MCCXXXV'] +   \
                     ['invalid input' for i in range(2*6)] +                \
                     ['I', 'V', 'V']

        truth_dict = {test_cases[i]:truth_vals[i] for i in range(len(test_cases))}
        for test_str in test_cases:
            try:
                result = self.check_arabic(test_str)
                assert (result == truth_dict[test_str]),    \
                      f'Failed test: {test_str}\n'+         \
                      f'  Result: {result}\n'      +        \
                      f'  Truth:  {truth_dict[test_str]}\n'
            except AssertionError as error:
                print(error)


    def __init__(self):
        print('Running test cases: ')
        self.test_arabic2roman()
        print('x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x\nTesting over')

# ArabicRomanConverter()
