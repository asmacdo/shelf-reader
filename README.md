[![Build Status](https://travis-ci.org/asmacdo/shelf-reader.svg?branch=master)](https://travis-ci.org/asmacdo/shelf-reader)

###About
Shelf Reader is a tool for libraries that retrieves call numbers of items 
from their barcode and determines if they are in the correct order. Because
it can search by barcode the script allows library staff to connect a 
barcode reader to quickly and accurately scan their shelves for items that 
are out of place.

This concept is not new, it has probably been around since libraries began
to digitize their records, but I have not been able to find a free open 
source implementation.

###Use

Get a dump of barcodes and call numbers and save them in a csv file with
barcodes in the left column and call numbers in the right. Either name the
file numbers.csv or adjust the name in shelf_reader.py. 

The project requires no depenencies (except nose if you want to run the tests). 
Make sure that you have python installed (tested for 2.6 and 2.7). 

To run, from the project directory:

    python shelf_reader.py
    
To run the tests:

    python run_tests.py