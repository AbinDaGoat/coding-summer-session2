"""
boolean logic is very necessary in order to better understand how conditional statement works

but what are conditional statements?

conditional statements are also known as branching statements, and they evaluate a different block of code
depending on the boolean expressions that are present
NOTE: conditional statements are resolved top-down

format of the language:

if boolean-expression-1:
    ... do something ...
elif boolean-expression-2: # elif is short for else if
    ... do something else ...
...
elif boolean-expression-n:
    ... do something else ...
else: # default case
    ... do the default case ...

the first if statement is required -- all other statements can be omitted

NOTE: conditional statements are mutually exclusive (disjoint) --> if one occurs, then the others do not

EXAMPLE 1:
coin flip

if (heads):
    do what we need to do for heads
else: # tails
    do what we need to do for tails

BAD DESIGN:

if (heads):
    do heads
elif (tails):
    do tails

EXAMPLE 2:
rock paper scissors

if (rock):
    do rock
elif (paper):
    do paper
else:
    do scissors

NOTE: illogical for this case
if (rock):
    do rock
if (paper):
    do paper
if (scissor):
    do scissor

EXAMPLE 3:
lottery system
consider the following situation:
there is a lottery system in your county where we have prizes for various categories of winners:
1st place --> 1 million pennies
2nd place --> 2 million dollars
3rd place --> ps5 box with a ps4 inside
4th place --> a high five from the pope

if (you are first place):
    get 1 million pennies
elif (you are second place):
    get 2 million dollars
elif (you are third place):
    get a ps5 box with a ps4 inside
elif (you are fourth place):
    get a high five from the pope

EXAMPLE 4:
tournament

if (you win the tournament):
    get winner prize

NOTE:
< and >= are opposite operators
> and <= are opposite operators

"""

x = 5

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

"""
from lines 83 to 88, that is called an if block (specifically its if-elif-else block)
"""

"""
DESIGN:

boolean variables should have names that are predicates --> verb phrase
examples:
1) is_ugly
2) is_set
3) is_running
4) is_unit_test_passing

RECALL:
functions also have a naming structure --> they are also verb-like, but not predicates
1) def display_name():
2) def get_user_age():
3) def calc_tip():

RECALL:
any other kind of variable should be noun-like ALWAYS:
examples:
1) tip
2) velocity
3) damage
"""

"""
nested if statements:

you can have anything in the block of code dedicated to each if-elif-else block; including other
conditional statements!!!

NOTE:

modulo operator: 
MATH:
    n mod m --> divide n by m, and get the remainder
    ex: 10 mod 5 --> 0
    ex: 7 mod 2  --> 1
    ex: 26 mod 7 --> 5

CODE:
    n % m --> divide n by m, and get the remainder
    ex: 10 % 5   --> 0
    ex: 7 mod 2  --> 1
    ex: 26 mod 7 --> 5
"""

x = 7

if x > 0: # check to see if its positive
    print("x is positive!!")
    # now determine if x is even --> use the modulo operator
    if x % 2 == 0:
        print("x is even!")
    else:
        print("x is odd!")
else:
    print("x is not positive!!")














