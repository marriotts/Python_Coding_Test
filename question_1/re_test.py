#!/usr/local/bin/python3

###############################################################################
#  Interview Python Coding Test Q1 - RegExp test
#
# Python Version:
# Using Python version3.5.1
#
# Editor:
# TextWrangler a product of Bare Bones Software, Inc.
# version 5.0.2 (3786)
# copyright ©1992-2015 Bare Bones Software, Inc.
# Registered to Simon Marriott
#
# Running on MacBook Pro with:-
#     System Version:   OS X El Capitan 10.11.3
###############################################################################

import re


# Global variables
###############################################################################
task = ''                # Holds the task number
regexp = ''              # Holds the regular expression
test_data = []           # Create an empty list to hold test data
dat_path = '.'           # Location of test data
match_str = ''           # The string to match
log_file = dat_path + '/q1_re_test_log.txt'
tst_dat_file = dat_path + '/re_test_data.txt'

# Functions
###############################################################################


def match_data(job, regex):
    # Append output data to log file with file handle 'log'
    try:
        log = open(log_file, "a")
    except IOError:
        print('Failed to open file {}.'.format(log.name))
    log.write(job + "\n")

    for element in test_data:
        mo = re.match(regex, element)
        if (mo):
            log.write(element + "\nMATCH:  " + regex + "\n")
        else:
            log.write(element + "\nNO MATCH\n")
    log.write('\n')    # Seperate solutions in the log file
    log.close()


# Main
###############################################################################

'''Open test data and copy to an array one line per element, dat is the file
handle "r" in the open command means read. "w" would be write and "a" would
be append.'''

try:
    dat = open(tst_dat_file, "r")
except IOError:
    print('Failed to open file {}.'.format(dat.name))

# Read test data to a list and remove whitespace line end char
for line in dat.readlines():
    test_data.append(line.rstrip('\r\n').strip())
dat.close()                  # Close the test data file

# Create a log file to capture the results
try:
    log = open(log_file, "w")
except IOError:
    print('Failed to open file {}.'.format(log.name))

log.write('Question 1 - Regular Expression Test\n')    # Add title
log.write('\n')                                                # Add new line
log.close()                                                    # Close log file

''' Task W1) Write a regexp that only matches the string (wherever
    it occurs):
        ABC'''

task = 'Solution 1:'
regexp = r'ABC'
match_data(task, regexp)    # Match data in function

''' Task W2:
    Write a single regexp that matches any of the strings below, and no
    others:
        ABC ACC ADC AXC'''

task = 'Solution 2:'
regexp = r'A[B|C|D|X]C'
match_data(task, regexp)    # Match data in function

''' Task W3:
    Write a regexp that will only matches the following string
    (when it is on a line entirely by itself):
        ABC'''

task = 'Solution 3:'
regexp = r'^ABC$'
match_data(task, regexp)    # Match data in function

''' Task W4:
    Write a regexp that matches any and only the strings that
    start A, and end with B, with anything inbetween.
     Make note of any assumptions that you make.'''

# Assuming that line end '\n' is not between A and B '.*' matches any char,
# except '\n', zero or more times.
task = 'Solution 4:'
regexp = r'^A.*B$'
match_data(task, regexp)    # Match data in function

''' Task W5:
    Write a regexp that matches any and only the strings that start
    with A, and end with B, with a run of one or more of either "XO" or "OX"
    in-between.'''

task = 'Solution 5:'
regexp = r'^A(XO|OX)+B$'
match_data(task, regexp)    # Match data in function
