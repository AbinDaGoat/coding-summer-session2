"""
so in python so far, we have been able to use the core set of functions that we have freely available:

print, input, type, etc...

however, there are times when we will want to access more "specialized" functions: think of sine and cosine and tangent!

thankfully, python supports the ability to import specialized functions from elsewhere. these are called modules

a module (also called a library) is a python file (or set of files) that contains code that has some level of
functionality

so why do we care about modules? because we don't need to define the sine function ourselves -- we just need to use it!

and in order to use it, we need to bring the features (functions and variables and everything else they have)
into our program
"""

"""
one example module we want to use is the math module

we bring the functions and variables and features in that module into our program by using an import statement
"""

import math # asks python to give us access to all of the functions in the "math" module

# now run the "sin" function defined inside the math module
# we first have to tell python to look inside of the "math" module to find the definition of the sin function
# we use the "dot" operator / character followed by the name of the feature we want to access

print("sin of pi (inaccurate) is", math.sin(3.1415))

# BETTER:
print("sin of pi (accurate) is", math.sin(math.pi))

print("this is pi:", math.pi)
print("e (euler's number):", math.e)

# some more examples:
print("sin of 90 degrees:", math.sin(math.radians(90)))


