import csv
from models import CallNumber
from ui import incorrect, correct, get_next_callnumber

FILE_NAME = "numbers.csv"
"""
name of csv file with barcodes and call numbers.
"""


def create_dictionary(filename):
    """
    Creates a dictionary from a csv file containing the catalog of barcodes in 
    the first column and call numbers in the second column.
    
    :param filename:    name of csv file
    
    :returns:           dictionary of barcodes and call numbers       
    """
    
    with open(filename, mode='r') as infile:
        reader = csv.reader(infile)
        return {rows[0]: rows[1] for rows in reader}


if __name__ == "__main__":

    barcode_dict = create_dictionary(FILE_NAME)
    call_a = CallNumber(get_next_callnumber(barcode_dict))
    call_b = CallNumber(get_next_callnumber(barcode_dict))

    while call_a < call_b:
        correct(call_a, call_b)
        call_a = call_b
        call_b = CallNumber(get_next_callnumber(barcode_dict))
    incorrect(call_a, call_b)