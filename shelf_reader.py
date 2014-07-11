import csv

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


def get_call_number(call_number_lookup):
    """
    Prompts the user for a barcode and returns the appropriate call number. If
    the user inputs a barcode that is not in the dictionary, the user is
    prompted again.

    :param call_number_lookup:  dictionary of barcodes and call numbers

    :returns:                   call number that matches user input barcode
    """

    barcode = raw_input("Barcode >>> ")

    while barcode.lower() != 'exit':

        call_number = call_number_lookup.get(barcode)

        if call_number is not None:
            return call_number
        else:
            print "Barcode does not have an associated call number"
            barcode = raw_input("Barcode >>> ")

    exit()


def check_type(c):
    """
    Checks the type of character of the input.
    
    :param c:   character to check
    
    :returns:    0 if letter, 2 if space, or 1 if number
    """
    
    if c.isalpha():
        return 0  # letter
    elif c == ' ':
        return 2  # space
    else:
        return 1  # number


def break_call_number(call_number):
    """
    Breaks a call number into tokens by inspecting each character of the call
    number and determining whether the character should be added to the
    previous token or if it should start a new token. Also adds a decimal to
    numbers that should be treated as decimals but do not already have one.
    
    :param call_number: the call number to be broken
    
    :returns broken:    a comma seperated list of tokens containing like
                        characters.
    """
    
    tokens = []
    new_token = call_number[0]

    for i in range(len(call_number) - 1):
        c = call_number[i]
        d = call_number[i + 1]
        if check_type(c) == check_type(d):  # d should be added to part of previous token
            new_token += d
        else:
            if check_type(new_token) != 2:  # Prevents adding a space as a token
                tokens.append(new_token)  # Adds completed token to the list

            if (check_type(c) == 0) and (check_type(d) == 1) and (i > 1):
                """
                Numbers following a letter other than the first letter are
                treated as decimals
                """
                
                d = '0.' + d
                
            new_token = d
            
    tokens.append(new_token)        
    return tokens


def is_correct(call_a, call_b):
    """
    Compares two call numbers and determines if they are in the correct order.
    
    :param call_a:  first call number
    
    :param call_b:  second call number
    
    :returns:       True if in the correct order, False otherwise
    """
    
    for i in range(len(call_a)):
        if call_a[i] != call_b[i]: 
            if not call_a[i] <= call_b[i]:
                return False
            return True
    return True


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
    
    call_number_lookup = create_dictionary(FILE_NAME)
    call_a = break_call_number(get_call_number(call_number_lookup))
    call_b = break_call_number(get_call_number(call_number_lookup))
    
    while is_correct(call_a, call_b):
        correct(call_a, call_b)
        call_a = call_b
        call_b = break_call_number(get_call_number(call_number_lookup))
    incorrect(call_a, call_b)

main()