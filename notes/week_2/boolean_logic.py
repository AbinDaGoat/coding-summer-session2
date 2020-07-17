"""
so far we have discussed statements, variables, types, and functions

today, we will be looking into discussing boolean operations

a field of math called discrete math --> goes into details on boolean operators and operations

two values for booleans: True, False

basic logical operators:

== --> equals
!= --> not equals
<  --> less than
>= --> greater than or equals
>  --> greater than
<= --> less than or equals

Examples:
1) 3 == 4   [False]
2) 3 <= 3   [True]
3) 17 != 17 [False]
"""

# will_the_world_end = 3 == 3 # True
# print("will the world end bro?", will_the_world_end)

"""
more complicated logical expressions:

more operators:

and --> logical and
or  --> logical or
not --> logical negation

for AND: # everything must be True for the entire expression to be True

True and False  --> False
False and True  --> False
True and True   --> True
False and False --> False

for OR: # only one expression must be True fo the entire expression to be True

True or True   --> True
True or False  --> True
False or True  --> True
False or False --> False  

for NOT:

not True  --> False
not False --> True

OPTIONAL:
short-circuiting is what python (and most other languages) do when evaluating logical expressions
--> if one sub expression of a chain of ors is True, then all other sub expressions are not evaluated
--> if one sub expression of a chain of ands is False, then all other sub expressions are not evaluated

"""

# is_coding_fun = (3 != 5) or (9 > 19) # short-circuiting is happening here
# print(is_coding_fun)

another_boolean = (19 >= -10) and (17 < 5) # --> True and False --> False
print(another_boolean)
print(not another_boolean)

"""
the following lines are equivalent:

line 1: x - 1 >= 2 and y * 3 <= 4
line 2: ((x - 1) > 2) and ((y * 3) <= 4) 

"""

