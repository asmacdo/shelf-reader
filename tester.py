"""
Before running, comment out main() in shelf_reader.py
"""

from shelf_reader import *
import csv

FILE_NAME = 'dewey_test_cases.csv'

test_dictionary = create_dictionary(FILE_NAME)


for line in range(2, len(test_dictionary) + 1):
    call_a = break_call_number(test_dictionary['1'])
    call_b = break_call_number(test_dictionary[str(line)])
    if (is_correct(call_a, call_b) == True):
        print "Pass"
    else:
        print "Fail"
        print call_a
        print call_b
    if(is_correct(call_b, call_a) == False):
        print "Pass"
    else:
        print "Fail"
        print call_a
        print call_b