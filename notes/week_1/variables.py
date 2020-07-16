"""
this is called the docstring of the file / application
it is supposed to represent what is done in this program

Variables:

variables in python hold different values. this means that they have
some sort of Type

Some Types (builtin):

int --> integer
bool --> boolean (true or false)
float --> floating point (basically a decimal)
double --> decimal (also the same thing as a floating point)
str --> string (of text)

NOTE:
    1) double is more precise than float (1 / 3 -> 0.3333333...)
    2) language is made up of characters, and a string of
        characters makes up words, and strings of words
        make up sentences --> string is just text

RULES:
--> variables are case sensitive
--> they must contain letters, numbers, and underscores ONLY
    ex:
    x = 10 # GOOD
    !xXBadassXx! = 10 # BAD
--> they cannot contain special characters
--> they cannot contain spaces
--> they should (basically, must) have meaningful names. Ignore examples that I use when we program

Example 1: tip calculator

GOOD NAMES:
total_amount = 420.69
tip = 21

BAD NAMES:
x = 420.69
y = 21

Example 2: video games

GOOD NAMES:
velocity = 12.8 # float
damage = 10 # int
hp = 6000 # int

BAD NAMES:
v = 12.8
d = 10
h = 6000

L-VAL vs. R-VAL

L-val is the value on the lhs of the equal sign.
R-val is the value on the rhs of the equal sign.

The equal sign is called the assignment operator (never say equal sign again).
This is NOT equality, it is assignment.

It means the variable on the lhs will HOLD the value determined on the rhs.

Ex:

x = 10
# here the value of x is 10
x = x + 1 # in math, this is a fallacy --> 0 = 1

In python, we execute the instructions from the top of the file to the bottom of the file. Line 68 occurs before
line 70.

In line 67, there is no variable called x.
After line 68, x holds the value of 10.
Starting before line 70, x holds the value of 10.

When line 70 starts, the rhs gets executed first. So x holds the value of 10 still. The value of the rhs is 11.
So then x gets REASSIGNED to the value of 11.

So in line 71, x holds the value of 11.

That is why r-val occurs BEFORE l-val.

"""

x = 10
y = 15

# z = x + y
# print(z)

z = 18
# z += 1 # this is better than z = z + 1

# z = (x + y) + z # 10 + 15 + 18
z += x + y # this is equal to line 96

# PEMDAS -> precedence

# z = x + y * (x - y) / z



print(z)

















