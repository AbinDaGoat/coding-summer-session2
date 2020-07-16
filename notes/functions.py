"""
the purpose of this lesson is to learn about functions

functions are of two forms (more than two but we will consider only two): built-in and user-defined

built-in: (provided by the system - python)
examples:
-> print()
-> type()

in math: a function is a relation in which for every input, there is a unique output

in code:
    a function is a relation in which 0 or more inputs perform a specific action, and 0 or more outputs may be given
    as long as an action is performed (i.e. functionality). that is, a function has served its purpose
    any task that must be done should be done in a function

NOTE: a function should have ONLY one purpose --> do not write functions with multiple tasks to perform

RULES:
--> the rules of naming functions is EXACTLY the same way as the rules of variables
--> there are some other things to consider when dealing with functions, which we will see later

SKELETON:

def function_name(parameter1, parameter2, ...):
    ... this is where the code to the function goes ...

"""

"""
Notes on Functions

--> there are two parts of any function:
1) defining a function: telling the system what the function does // function definition
2) calling a function: using the function itself // function call
"""

"""
Built-in functions:

for built-in functions, the definition is already in the python environment i.e. the system already knows what that
    function does
all we need to do is use it (call it)
"""

"""
Functions in MATH:
ex 1: 
f(x) = 2x + 4
  ^
that x is called the parameter / argument of the function --> it's anything you pass into it

f(2) = 2 * 2 + 4 = 8
f(-5) = 2 * (-5) + 4 = -6

ex 2:
f(x, y) = 3x - 7y + xy ==> x and y are called parameters, f is the name of the function

f(0, 1) = 3 * 0 - 7 * 1 + 0 * 1 = -7
f(1, 1) = 3 - 7 + 1 = -3

z = f(1, 1)
z holds the value of -3

IN CODE:
a function can have zero or more parameters
a function does not NEED to output / return anything back to you 

"""

# this is a builtin function, and it does not return anything
# it only outputs to the screen
# print("check me out right")
# print() # prints out a newline character
# print("here")

# x = 15
# print(x)

# print can have any number of arguments

# z = 16. # this is a decimal
# print("my variable z holds the value of", z)

# type_of_z = type(z) # lval vs rval
# print("the type of my variable z is", type_of_z)
# print("the type of my variable z is", type(z))

# is_smart = True # True and False are keywords --> they hold a boolean
# print("am i really smart?", is_smart)
# print("whats the type of the smart?", type(is_smart))

"""
TAKEAWAYS:
--> keywords cannot be used as variable names
--> how the print function works
--> how the type function works
"""

# print("whats happening here?", type()) # type function NEEDS either 1 argument or 3 arguments

"""
USER DEFINED FUNCTIONS:
"""

# function definition (from lines 108 to line 114)
def random_function(argument1, argument2): # this is called the function prototype
    # this line
    # this line
    # and even this line
    # are all a part of the function definition of the function random_function
    x = 15
    y = 17
    print("i am inside random_function and i am getting called")

"""
not all functions must return something
recall:
- print doesnt return anything, but it outputs to the screen (this is the "task" that it performs)
- type does return something, it returns what the type of the variable passed in as an argument is

how do we return something: using the return keyword
"""

# if i want to call this function: i need to use its name and pass in any required arguments
# random_function(10000000, -420.69)


def f(x): # defining f
    y = 2 * x + 4
    # y holds the value of 8


# my_val = f(2) # calling f
# print("what is my_val?", my_val) # this is a None --> it's type is NoneType


def better_f(x):
    y = 2 * x + 4
    return y

# better_my_val = better_f(2)
# print("this is what better_my_val is", better_my_val)

"""
define a function of the form:
g(x, y) = 3x - 7y + xy 
"""

def g(x, y):
    z = 3 * x - 7 * y + x * y
    return z

some_val = g(0, 1) # return -7
new_val = some_val + 27

print("some_val =", some_val)
print("new_val =", new_val)






