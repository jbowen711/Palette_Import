import os
import csv
"""
functions to read the a CSV file
and put it into a dictionary
"""

def read_palette_from_file(palette_filename):
    """
    read the palette from the csv file.
    Each row is a key and an RGB triple.  Make that RGB triple
    into a TUPLE and then put into a dictionary with the key.
    """
    my_dict = dict()
    with open(palette_filename, 'r') as in_file:
        csv_reader = csv.reader(in_file)
        for row in csv_reader:
            key = int(row[0])
            red = int(row[1])
            green = int(row[2])
            blue = int(row[3])
            value = (red,green,blue)
            my_dict[key] = value
    print(my_dict)
    return(my_dict)
