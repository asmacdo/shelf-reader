import csv
from models import CallNumber

FILE_NAME = "numbers.csv"
"""
name of csv file with barcodes and call numbers.
"""


def create_dictionary(filename):
    """
    Creates a dictionary from a csv file containing the catalog of barcodes in 
    the first column and call numbers in the second column. Creates a dictionary 
    from the first two columns of the csv file.
    
    :param filename:    name of csv file with barcodes and call numbers
    
    :returns:           dictionary of barcodes and call numbers       
    """
    
    with open(filename, mode='r') as infile:   
        reader = csv.reader(infile)
        return {rows[0]: rows[1] for rows in reader}


def get_next_callnumber(barcode_dict):
    """
    Prompts the user for a barcode and returns the appropriate call number. If
    the user inputs a barcode that is not in the dictionary, the user is
    prompted again.

    :param barcode_dict:  dictionary of barcodes and call numbers

    :returns:                   call number that matches user input barcode
    """

    barcode = raw_input("Barcode >>> ")

    while barcode.lower() != 'exit':

        call_number = barcode_dict.get(barcode)

        if call_number is not None:
            return call_number
        else:
            print "Barcode does not have an associated call number"
            barcode = raw_input("Barcode >>> ")

    exit()


def correct(call_a, call_b):
    """
    Informs the user that the order is correct.
    
    :param call_a:  first call number - not used at this time but could be
                    important in later versions.
                    
    :param call_b:  second call number - not used at this time but could be
  
                  important in later versions.
    """
    
    print "_________________________________"
    print "|                                |"
    print "|             Correct            |"
    print "|                                |"
    print "|________________________________|"


def incorrect(call_a, call_b):
    """
    Informs the user that the order is incorrect and provides the call numbers
    so the user can do a manual check.
    
    :param call_a:  first call number
    
    :param call_b:  second call number
    """
    
    print "_________________________________"
    print "|                                |"
    print "|             Incorrect          |"
    print "|                                |"
    print "|________________________________|"
    print call_a
    print call_b
    print
    
    
def main():
    """
    Creates a dictionary of call numbers and barcodes, gets call numbers from
    input barcodes and determines if the call numbers are in the correct order.
    Calls the correct() and incorrect() methods accordingly. If correct, promts
    the user for another barcode.
    """
    
    barcode_dict = create_dictionary(FILE_NAME)
    call_a = CallNumber(get_next_callnumber(barcode_dict))
    call_b = CallNumber(get_next_callnumber(barcode_dict))
    
    while call_a < call_b:
        correct(call_a, call_b)
        call_a = call_b
        call_b = CallNumber(get_next_callnumber(barcode_dict))
    incorrect(call_a, call_b)

if __name__ == "__main__":
    main()