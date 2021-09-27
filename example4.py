#!python

"""
Note that when working with logical operators, each 
partial statement must have its own operator:
"""
# The following code is valid:

x = 3
y = 4

if x > 3 and x > 5:
    print("x is greater than both of them")


# The following code will throw an error:
if x > 3 and 5:
    print("This contains an error and will not work")