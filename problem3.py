#! python3
"""
Problem 3
Pythagorean triples are sets of 3 integers such that the squares of the 2 smaller numbers is equal to the square of the third.
Ask the user to enter in 3 numbers, in any order.  Order the numbers from smallest to largest.
Determine if they form a Pythagorean triple. 

You can use max() to help you find the largest number
You can use min() to help you find the smallest number
How can we find the middle number though?
(2 marks)

Inputs:
an integer
an integer
an integer

Outpus:
xx,yy,zz form a Pythagorean Triple
xx,yy,zz do not form a Pythagorean Triple

Examples:
Enter an integer=>3
Enter an integer=>5
Enter an integer=>4
3,4,5 form a Pythagorean triple

Enter an integer=>5
Enter an integer=>4
Enter an integer=>2
2,4,5 do not form a Pythagorean triple
"""
a = float(input("Please enter a number."))
b = float(input("Please enter another number."))
c = float(input("Please enter a final number."))

formed = False
if a**2 + b**2 == c**2:
    formed = True
elif b**2 + c**2 == a**2:
    formed = True
elif a**2 + c**2 == b**2:
    formed = True

if a > b and b > c:
    biggest = a
    middle = b
    smallest = c
elif c > b and b > a:
    biggest = c
    middle = b
    smallest = a
elif b > c and c > a:
    biggest = b
    middle = c
    smallest = a
elif a > c and c > b:
    biggest = a
    middle = c
    smallest = b


if formed == True:
    print(str(int(smallest)) + "," + str(int(middle)) + "," + str(int(biggest)) + " form a Pythagorean triple")
else:
    print(str(int(smallest)) + "," + str(int(middle)) + "," + str(int(biggest)) + " do not form a Pythagorean triple")