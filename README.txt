Interview Python Coding Tests - Simon Marriott

Introduction:
All of my work for these tests has been carried out on my MacBook Pro, running OS X
El Capitan version 10.11.3 (15D21), and I began the test on Monday 21st March 2016.

My shebang in each python script is #!/usr/local/bin/python3

I am using Python version 3.5.1, and my text editor is TextWrangler Version 5.0.2 (3786)
by Bare Bones Software.

My usual starting point with Python, or any scripting language,
is 'Don't re-invent the wheel!':-
    Identify modules that may make your life easier when solving your problem
    Google and stackoverflow are your friends - Someone may already have a solution that
    either solves your problem or comes close and requires some adaption.  Be aware of
    licensing issues!!
If none of these help, then write your own code.

Question 1: Regular Expression Test


Question 2: File Searching Test:-
F1) Core task:

I have used python modules sys, os, re to complete this task.  However I am not using
os.walk() or os.scanf() methods

For iterating over a directory tree, there are simple methods to do this e.g. os.walk(),
os.scandir() and glob.glob and minimise the amount of code and time taken.  I have used
methods from package 'os' like listdir(), islink(), isfile() and isdir() in my own
recursive function.

F2) Non-Cyclic Links:
In my script, I have used the os.islink() method to check for symboiclinks and skipped
the item if this returned True.

To avoid duplicate .inform files on Unix/Linux/OS X systems, you could:-
    1) Get the inode number of a file using either os.stat() or os.fstat() methods,
    the inode number is the second element of the returned data structure. by
    concatonating this number with the file name, duplicates could be eliminated by
    saving the filename in a set.
    2) You could use hashing using the hashlib module to create a hash of the file
    and compare wwith other hashed files to find duplicates.

Question 3 - ISO8601 Time/Date Parser
References:-
Wikipedia - https://en.wikipedia.org/wiki/ISO_8601
ISO - http://www.iso.org/iso/home/standards/iso8601.htm

So,I would use regexp to solve this conundrum, implementing named groups e.g.
(?P<group_name>…), to isolate relevent sections of an input ISO time/date string.
I have made two attempts at this withoutcomplete success.

My regexes would not have incuded +/- before the year i.e. no negative years.
