#!/usr/local/bin/python3

###############################################################################
# Interview Python Coding Test Q3 ISO8601 Parser Test
#
# Python Version:
#     Using Python version 3.5.1
#
# Editor:
#     TextWrangler, a product of Bare Bones Software, Inc.
#     version 5.0.2 (3786)
#     copyright ©1992-2015 Bare Bones Software, Inc.
#     Registered to Simon Marriott
#
# Running on MacBook Pro with:-
#     System Version:   OS X El Capitan 10.11.3
###############################################################################

#import datetime
#from decimal import Decimal
#import sys
import re


# Global variables
###############################################################################


# Functions
###############################################################################


# Main
###############################################################################

# Get time/date from stdin
#inpstring = input('Please Enter a time:\n')

test_str = '2000-08-12T12:00:00'

# Split Time and date not including negative years!
datetime_re = r'(?P<date>.*?)[ T](?P<time>.*)$'

year_regex = r'(?P<year>[0-9]{4})'
year_mm_regex = (r'''(?P<year_mm>([0-9]{4}-[0-9]{1,2})) # yyyy-mm
                    (^(?P<yearmm>([0-9]{4}[0-9]{1,2})))  # not yyymm
                    ''', re.VERBOSE)
month_regex = r'((-(?P<month>(([0-9]{1,2}) | ([0-9]{2})))))'
day_regex = r'((-(?P<daysep>[0-9]{1,2})) | (?P<day>[0-9]{2}))'
hour_regex = r'(?P<hour>[0-9]{2})'
mins_regex = r'(:{0,1}(?P<minute>[0-9]{2}){0,1})'
sec_regex = r'(:{0,1}(?P<sec>[0-9]{1,2})([.,](?P<sec_dec>[0-9]+)){0,1}){0,1}'
tzone_regex = (r'''(?P<timezone>Z | ((?P<tz_sign>[-+]))
                    (?P<tz_hour>[0-9]{2}):{0,1}(?P<tz_minute>[0-9]{2}){0,1})
                    ){0,1}''', re.VERBOSE)
# Split test date/time
tdm = re.match(datetime_re, test_str)
if tdm:
    date = tdm.group("date")
    time = tdm.group("time")
    yr = re.match(year_regex, date)
    if yr:
        year = (yr.group("year"))
        century = str(int(year[:2]) + 1)
        print('Century: {}'.format(century))
        print('Year: {}'.format(yr.group("year")))
    else:
        print('Century: {}'.format('Undefined'))
        print('Year: {}'.format('Undefined'))
    mth = re.match(month_regex, date)
    if mth:
        print('Month Matched')
        if mth.group("monthsep"):
            print('Month: {}'.format(mth.group("monthsep")))
        elif mth.group("month"):
                print('Month: {}'.format(mth.group("month")))
    else:
        print('Month: {}'.format('Undefined'))
else:
    print('No Match\n')
