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

iso_regex = (r'''
                (?P<year>\d{4})
                (-(?P<month>\d{1,2}) | (\d{2}))
                (-(?P<day>\d{1,2}) | (\d{2}))
                ([\sT](?P<hour>\d{1,2}))
                (:{0,1}(?P<minute>\d{1,2}))
                (:{0,1}(?P<second>\d{1,2})([.,](?P<millisec>\d+)){0,1})
            ''', re.VERBOSE)

# Split test date/time
mo = re.match("iso_regex", test_str)
if mo:
    if mo.group("year"):
        century = str(int(mo.group("year")[:2]) + 1)
        print('Century: {}'.format(century))
        print('Year: {}'.format(mo.group("year")))
    else:
        print('Century: {}'.format('Undefined'))
        print('Year: {}'.format('Undefined'))
    if mo.group("month"):
        print('Month: {}'.format(mo.group("month")))
    else:
        print('Month: {}'.format('Undefined'))
    if mo.group("day"):
        print('Day: {}'.format(mo.group("day")))
    else:
        print('Day: {}'.format('Undefined'))
    if mo.group("hour"):
        print('Hour: {}'.format(mo.group("hour")))
    else:
        print('Hour: {}'.format('Undefined'))
    if mo.group("minute"):
        print('Minute: {}'.format(mo.group("minute")))
    else:
        print('Minute: {}'.format('Undefined'))
    if mo.group("second"):
        print('Second: {}'.format(mo.group("second")))
    else:
        print('Second: {}'.format('Undefined'))
    if mo.group("millisec"):
        print('Millisecond: {}'.format(mo.group("millisec")))
    else:
        print('Millisecond: {}'.format('Undefined'))
else:
    print('No Matches\n')
