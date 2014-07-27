.. image:: https://travis-ci.org/asmacdo/shelf-reader.svg?branch=master
    :target: https://travis-ci.org/asmacdo/shelf-reader

============
Shelf Reader
============

Shelf Reader is a tool for libraries that retrieves call numbers of items 
from their barcode and determines if they are in the correct order. Because
it can search by barcode the script allows library staff to connect a 
barcode reader to quickly and accurately scan their shelves for items that 
are out of place.

This concept is not new, it has probably been around since libraries began
to digitize their records, but I have not been able to find a free open 
source implementation.

Install
-------

.. code-block:: bash

    $ pip install shelf-reader

Requires Python >= 2.7

Use
---

Get a dump of barcodes and call numbers and save them in a csv file with
barcodes in the left column and call numbers in the right. 

The project requires no depenencies (except nose if you want to run the tests). 
Make sure that you have python installed (tested for 2.6 and 2.7). 

To run:

.. code-block:: bash

    $ shelf-reader path/to/filename.csv

License
-------

GPL 2
