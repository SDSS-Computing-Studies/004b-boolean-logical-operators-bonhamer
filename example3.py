#! python3

"""
When working with conditional operators that have brackets,
each bracket is evaluated first until you have a single 
statement with only "and" and "or" statements.
"""

print("=======================================")
print(" Example 3: logical operations ")
a = 5
b = 10
c = 5
if (a==5 and b==10) or c == 3:
  print("Overall, the condition is True")
else:
  print("Overall, the condition is False")
print("=======================================")
