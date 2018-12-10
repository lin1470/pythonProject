#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Your task in this exercise is to modify 'extract_carrier()` to get a list of
all airlines. Exclude all of the combination values like "All U.S. Carriers"
from the data that you return. You should return a list of codes for the
carriers.

All your changes should be in the 'extract_carrier()' function. The
'options.html' file in the tab above is a stripped down version of what is
actually on the website, but should provide an example of what you should get
from the full file.

Please note that the function 'make_request()' is provided for your reference
only. You will not be able to to actually use it from within the Udacity web UI.
"""

from bs4 import BeautifulSoup
import bs4
html_page = "options.html"


def extract_carriers(page):
    data = []

    with open(page, "r") as html:
        # do something here to find the necessary values
        soup = BeautifulSoup(html, "lxml")
        airPortList = soup.find(id = "CarrierList")
        children = airPortList.children
        for child in children:
            # print type(child)
            if not isinstance(child,bs4.element.NavigableString):
                data.append(child['value'])
            # print
        data.remove('All')
        data.remove('AllUS')
        data.remove('AllForeign')
        print len(data)
        print data
    return data


def make_request(data):
    eventvalidation = data["eventvalidation"]
    viewstate = data["viewstate"]
    airport = data["airport"]
    carrier = data["carrier"]

    r = s.post("https://www.transtats.bts.gov/Data_Elements.aspx?Data=2",
               data = (("__EVENTTARGET", ""),
                       ("__EVENTARGUMENT", ""),
                       ("__VIEWSTATE", viewstate),
                       ("__VIEWSTATEGENERATOR",viewstategenerator),
                       ("__EVENTVALIDATION", eventvalidation),
                       ("CarrierList", carrier),
                       ("AirportList", airport),
                       ("Submit", "Submit")))

    return r.text


def test():
    data = extract_carriers(html_page)
    assert len(data) == 16
    assert "FL" in data
    assert "NK" in data

if __name__ == "__main__":
    test()