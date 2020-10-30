#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2
a = input("input the furst number")
a = float(a)
b = input("input the second number")
b = float(b)
c = input("input the third number")
c = float(c)
x = c - b
x = float(x)
y = x / a
print(y)