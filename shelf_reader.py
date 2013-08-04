import csv
import re
from sys import argv

# File name of csc file containing barcodes and call numbers.
filename = "numbers.csv"

# Opens the csv file containing the catalog. Creates a dictionary from the
# first two columns of the csv file.
with open(filename, mode='r') as infile:
    reader = csv.reader(infile)
    call_number_lookup = {rows[0]:rows[1] for rows in reader}
	
# Prompts the user for a barcode and returns the appropriate call number.
def get_call_number():
	barcode = raw_input("Barcode>>>")
	call_number = call_number_lookup[barcode]
	return call_number

# Checks the type of character of the input. Returns 0 for letter, 1 for 
# number, or 2 for space. 
def check_type(c):
	letter_check = re.compile('[a-zA-Z]')
	if letter_check.match(c): # True if c is a letter
		return 0 #letter
	elif (c == ' '):
		return 2 # space
	else:
		return 1 # number
		
# Breaks a call number into tokens and removes spaces. Returns a list of the
# tokens.
def break_call_number(call_number):
	broken = []
	next = call_number[0]
	
	for i in range(len(call_number) - 1):
		c = call_number[i] #the last character inspected
		d = call_number[i + 1] # the next character to inspect
		if check_type(c) == check_type(d): # d is part of previous token
			next += d
		else:
			if check_type(next) != 2: # Prevents adding a space as a token
				broken.append(next)
			
			# Numbers following a letter other than the first letter are 
			# assumed to be decimals.
			if ((check_type(c) == 0) and (check_type(d) == 1) and (i > 1)):
				d = '0.' + d
			next = d				
	return broken
	

# Compares two tokens of the call number and determines if they are sorted
# correctly. 
# Returns True or False.
def is_sorted(a, b):
	if (check_type(a) == 1): # Number
		return (a <= b)
	else: # Letters
		not_sorted = [a, b]
		list = [a, b]
		list.sort()
		return (list == not_sorted)	

# Compares two call numbers and determines if they are in the correct order.
def is_correct(call_a, call_b):
	for i in range(len(call_a)):
		if call_a[i] != call_b[i]: 
			if not is_sorted(call_a[i], call_b[i]):
				return False
			return True
	return True
	
# Reaction to the correct order	
def correct():
	print "_________________________________"
	print "|                                |"
	print "|             Correct            |"
	print "|                                |"
	print "|________________________________|"

# Reaction to the incorrect order
def incorrect():
	print "_________________________________"
	print "|                                |"
	print "|             Incorrect          |"
	print "|                                |"
	print "|________________________________|"	
	
# Gets barcodes, converts to call numbers, and determines if the call numbers
# are in the correct order. Calls the correct() and incorrect() methods 
# accordingly. If correct, it gets another barcode.
def main():
	call_a = break_call_number(get_call_number())
	call_b = break_call_number(get_call_number())
	while is_correct(call_a, call_b):
		correct()
		call_a = call_b
		call_b = break_call_number(get_call_number())
	incorrect()
	
main()