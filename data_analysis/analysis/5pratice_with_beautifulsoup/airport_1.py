#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Complete the 'extract_airports()' function so that it returns a list of airport
codes, excluding any combinations like "All".

Refer to the 'options.html' file in the tab above for a stripped down version
of what is actually on the website. The test() assertions are based on the
given file.
"""

from bs4 import BeautifulSoup
html_page = "options.html"
import bs4

def extract_airports(page):
    data = []
    with open(page, "r") as html:
        # do something here to find the necessary values
        # soup = BeautifulSoup(html, "lxml")
        soup = BeautifulSoup(html, "lxml")
        airPortList = soup.find(id="AirportList")
        children = airPortList.children
        for child in children:
            # print type(child)
            if not isinstance(child, bs4.element.NavigableString):
                data.append(child['value'])
                # print
        print len(data)
        print data
        data.remove('All')
        data.remove('AllMajors')
        data.remove('AllOthers')

    return data


def test():
    data = extract_airports(html_page)
    assert len(data) == 15
    assert "ATL" in data
    assert "ABR" in data

if __name__ == "__main__":
    test()