#!/usr/local/bin/python3

###############################################################################
# Python Coding Test Q2 File Searching Test
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

import os
import re

# Global variables
###############################################################################
top = '.'                             # working dir
root = './files'                      # Root directory of tree to be searched
myfiles = []                          # Allocate array for holding found files
mylines = []                          # List of found files
port_count = {}                       # Dict for valid port num count
port_log = top + '/ports_log.txt'     # log file


# Functions
###############################################################################


def tree_search_inform(path):
    '''Searches the directory tree for *.inform files and saves them,
       with their path, in a list.  I also skip symbolic links here'''
    for item in os.listdir(path):
        if os.path.islink(os.path.join(path, item)):
            # Skip symbolic link to avoid duplicated files
            next
        elif os.path.isfile(os.path.join(path, item)):
            if item.endswith('.inform'):
                myfiles.append(os.path.join(path, item))
        elif os.path.isdir(os.path.join(path, item)):
            tree_search_inform(os.path.join(path, item))
        else:
            next


# Main
###############################################################################

tree_search_inform(root)

# There should be 6 .inform files in the test directory tree
#print(len(myfiles))                         # Use for debug

for file in myfiles:
    # Open file in file handler fh with readonly
    with open(file, "r") as fh:
        for line in fh:
            line = line.strip()  # Remove any whitespace
            ''' Validate hexadecimal number from 4 to 32
                characters and strip leading hash symbol
                using a reguar expression with group'''
            r = re.compile(r'^#([0-9A-Fa-f]{4,32})$')
            mo = r.match(line)
            '''If we find a valid port number, we want to
               calculate frequency a number occurs, so use a
               dictionary to do this.  I will also capitalise
               the port number for convenience.'''
            if mo:
                if mo.group(1).upper() not in port_count:
                    # Initialise key and set value to 1
                    port_count[mo.group(1).upper()] = 1
                else:
                    # Increment value
                    port_count[mo.group(1).upper()] += 1

# Create the log, there will be no missing file exception in this case
log = open(port_log, "w")
# Add a title to the log file
log.write("Interview Python Coding Test: Question 2 - Search Files\n")
log.write("\n")                                           # Add new line
log.close()                                               # Close the file

# Open log file to append the data
try:
    log = open(port_log, "a")
except IOError:
    print('File {} does not exist.'.format(log.name))

# Output results, ordered by length of Port Number, to the terminal
print('{:>32}\t{:2}'.format('Port', 'Frq'))
log.write('{:>32}\t{:2}\n'.format('Port', 'Frq'))
print('{:>32}\t{:3}'.format('----', '---'))
log.write('{:>32}\t{:3}\n'.format('----', '---'))

# Output the counts to the terminal and to the log file
for k in sorted(port_count, key=len):
    print('{:>32}\t{:>2}'.format(k, port_count[k]))
    log.write('{:>32}\t{:>2}\n'.format(k, port_count[k]))

log.close()                                          # Close the log file
