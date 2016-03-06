#!/usr/bin/env python
"""
Your task is as follows:
- read the provided Excel file
- find and return the min, max and average values for the COAST region
- find and return the time value for the min and max entries
- the time values should be returned as Python tuples

Please see the test function for the expected return format
"""

import xlrd
from zipfile import ZipFile
import numpy as np

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()

def max_and_index(input_list):
    #print(input_list)
    my_max = (0, input_list[0])
    for i, value in enumerate(input_list):
        if value > my_max[1]:
            my_max = (i, value)
    return my_max

def test_max_and_index():
    my_list = [0, 1, 3, 5, 2, 2]
    return max_and_index(my_list)

def min_and_index(input_list):
    my_min = (0, input_list[0])
    for i, value in enumerate(input_list):
        if value < my_min[1]:
            my_min = (i, value)
    return my_min

def max_in_col(sheet, col):
    sheet_values = sheet.col_values(col)
    times = [float(sheet_values[i]) for i in range(1, len(sheet_values))]
    return max_and_index(times)

def min_in_col(sheet, col):
    sheet_values = sheet.col_values(col)
    times = [float(sheet_values[i]) for i in range(1, len(sheet_values))]
    return min_and_index(times)

def avg_in_col(sheet, col):
    sheet_values = sheet.col_values(col)
    times = [float(sheet_values[i]) for i in range(1, len(sheet_values))]
    return np.mean(times)

def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    max_index, max_value = max_in_col(sheet, 1)
    min_index, min_value = min_in_col(sheet, 1)

    #print(max_index)
    #print(min_index)

    max_time = xlrd.xldate_as_tuple(sheet.cell_value(max_index + 1, 0), 0)
    min_time = xlrd.xldate_as_tuple(sheet.cell_value(min_index + 1, 0), 0)
    
    data = {
            'maxtime': max_time,
            'maxvalue': max_value,
            'mintime': min_time,
            'minvalue': min_value,
            'avgcoast': avg_in_col(sheet, 1)
    }
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)

