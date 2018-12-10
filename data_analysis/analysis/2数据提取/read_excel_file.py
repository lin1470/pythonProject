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

datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    # sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    ### other useful methods:
    # print "\nROWS, COLUMNS, and CELLS:"
    # print "Number of rows in the sheet:",
    # print sheet.nrows
    # print "Type of data in cell (row 3, col 2):",
    # print sheet.cell_type(3, 2)
    # print "Value in cell (row 3, col 2):",
    # print sheet.cell_value(3, 2)
    # print "Get a slice of values in column 3, from rows 1-3:"
    # print sheet.col_values(3, start_rowx=1, end_rowx=4)

    # print "\nDATES:"
    # print "Type of data in cell (row 1, col 0):",
    # print sheet.cell_type(1, 0)
    # exceltime = sheet.cell_value(1, 0)
    # print "Time in Excel format:",
    # print exceltime
    # print "Convert time to a Python datetime tuple, from the Excel float:",
    # print xlrd.xldate_as_tuple(exceltime, 0)
    # min_value = 80000
    # for i in range(1,sheet.nrows):
    #     test_a=sheet.cell_value(i,1)
    #     if test_a<min_value:
    #        min_value = test_a
    # print "the min_value is ",min_value
    #
    # max_value = 0
    # for i in range(1,sheet.nrows):
    #     test_b = sheet.cell_value(i,1)
    #     if test_b > max_value:
    #         max_value = test_b
    # print "the max_value is ", max_value
    #
    # sum_a = 0
    # for i in range(1,sheet.nrows):
    #     sum_a+=sheet.cell_value(i,1)
    # avgcoast = sum_a/(sheet.nrows-1)
    # print "the avgcoast is ", avgcoast
    #
    # min_time = 80000
    # for i in range(1, sheet.nrows):
    #     test_a = sheet.cell_value(i, 0)
    #     if test_a < min_time:
    #         min_time = test_a
    # min_time = xlrd.xldate_as_tuple(min_time,0)
    # print "the min_time is",min_time
    #
    # max_time = 0
    # for i in range(1, sheet.nrows):
    #     test_b = sheet.cell_value(i, 0)
    #     if test_b > max_time:
    #         max_time = test_b
    # max_time = xlrd.xldate_as_tuple(max_time,0)
    # print "the max_time is",max_time
    # data = {
    #     'maxtime': max_time,
    #     'maxvalue': max_value,
    #     'mintime': min_time,
    #     'minvalue': min_value,
    #     'avgcoast': avgcoast
    # }
    cv = sheet.col_values(1,start_rowx=1,end_rowx=None)
    #print cv
    min_val = min(cv)
    max_val = max(cv)
    min_pos = cv.index(min_val)+1
    max_pos = cv.index(max_val)+1
    max_time = sheet.cell_value(max_pos,0)
    real_max_time = xlrd.xldate_as_tuple(max_time,0)
    min_time = sheet.cell_value(min_pos,0)
    real_min_time = xlrd.xldate_as_tuple(min_time,0)
    avgcoast = sum(cv)/float(len(cv))
    data = {
        'maxtime': real_max_time,
        'maxvalue': max_val,
        'mintime': real_min_time,
        'minvalue': min_val,
        'avgcoast': avgcoast
    }
    return data


def test():
    #open_zip(datafile)
    data = parse_file(datafile)
    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()