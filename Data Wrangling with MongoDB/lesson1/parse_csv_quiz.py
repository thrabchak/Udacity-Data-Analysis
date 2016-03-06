# -*- coding: utf-8 -*-
# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on "," and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os

DATADIR = ""
DATAFILE = "beatles-discography.csv"
#DATAFILE = "beatles-diskography.csv"


def parse_file(datafile):
    headers = ['Title', 'Released', 'Label', 'UK Chart Position', 'US Chart Position', 'BPI Certification', 'RIAA Certification']
    data = []
    counter = 0
    with open(datafile, "r") as f:
        for line in f:

            line_dict = {}
            line_values = line.split(',', len(headers)-1)

            for i in range(0, len(line_values)):
                stripped_val = line_values[i].strip()
                #print headers[i] + ": " + stripped_val
                line_dict[headers[i]] = stripped_val

            if counter > 0 and counter < 11:
                data.append(line_dict)

            counter += 1

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert len(d) == 10
    
test()