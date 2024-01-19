# tell the unix style users where the Python interpreter lives
# so that you can run this file from the terminal

#!/usr/bin/python

# We use the standard CMD + / or CTRL + / for a comment
# Victoria's Anatomy Script
# Example Python script

# import a module with the 'import' keyword
# a module is a set of pre-written code
# 'sys' provides members that give is access to our device's sytem
import sys

# creating a variable called argument_count
# a variable is a placeholder in memory for data whose value can change
# arg c stands for argument count
# len - is a built-in function that calculates / returns the length of something
# argv is a member of the sys module
# argv is an argument vector - the list of arguments that are passed as inputs to our script
argument_count = len(sys.argv)

# if statements are conditional statements
# if the argument count is greater than 1
if argument_count > 1:
    print('Too many args')
#     otherwise do this
else:
    # create a new variable called 'where' and assign the string value of 'World' to it
    where = 'World'
    # print the strings "Hello" and the value of the 'where' variable
    # when we "add" strings it is called 'concatenation'
    # print takes a variable number of arguments
    # This is called a variadic function
    print("Hello", where)

# print the string 'Goodbye from ' concatenated to the zeroth argument from the vector
print('Goodbye from ' + sys.argv[0])

# this is how Python 2 used to print stuff
# print was a statement not a function
# print 'hello'


