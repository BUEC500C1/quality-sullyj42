#!/usr/bin/env python
'''
Convert an arabic number to a roman numeral

Usage:
>> converter = ArabicRomanConverter() # Instantiate class
>> roman     = converter('12')        # Convert an arabic string
-- XII
>> roman     = converter(12)          # Convert any valid numeric type
-- XII

Valid types are integers greater than 0
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
        This is the first of a waterfall of functions to convert

        This checks if an input is valid.
        -- If valid, calls the next function to convert the roman numeral
        -- If invalid, returns an error string prints debug info to stderr
        '''
        try:
            # First make a float so we can compare it to an int later
            num = float(arabic_str)

        except ValueError:
            if arabic_str == "":
                print(f'Invalid input -- no input provided', file=stderr)
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
        test_nums = list(num_map.keys())  # Pulls the arabic numbers
        test_nums.sort()
        while num > 0:
            roman2add = max([romans for romans in test_nums if num >= romans])
            roman_string.append(num_map[roman2add])
            num = num - roman2add

        self.roman_string = roman_string
        return ''.join(roman_string)

    def __init__(self, input_string):
        '''
        This is a constructor accepting a single string input
        '''
        self.arab_string = input_string
# ArabicRomanConverter()
