# -*- coding: utf-8 -*-
from __future__ import print_function
from .compat import user_input

def correct(call_a, call_b):
    """
    Informs the user that the order is correct.

    :param call_a:  first call number - not used at this time but could be
                    important in later versions.

    :param call_b:  second call number - not used at this time but could be

                  important in later versions.
    """

    print("_________________________________")
    print("|                                |")
    print("|             Correct            |")
    print("|                                |")
    print("|________________________________|")


def incorrect(call_a, call_b):
    """
    Informs the user that the order is incorrect and provides the call numbers
    so the user can do a manual check.

    :param call_a:  first call number

    :param call_b:  second call number
    """

    print("_________________________________")
    print("|                                |")
    print("|             Incorrect          |")
    print("|                                |")
    print("|________________________________|")
    print(call_a)
    print(call_b)
    print()


def get_next_callnumber(barcode_dict):
    """
    Prompts the user for a barcode and returns the appropriate call number. If
    the user inputs a barcode that is not in the dictionary, the user is
    prompted again.

    :param barcode_dict:  dictionary of barcodes and call numbers

    :returns:                   call number that matches user input barcode
    """

    barcode = user_input("Barcode >>> ")

    while barcode.lower() != 'exit':

        call_number = barcode_dict.get(barcode)

        if call_number is not None:
            return call_number
        else:
            print("Barcode does not have an associated call number")
            barcode = raw_input("Barcode >>> ")

    exit()
