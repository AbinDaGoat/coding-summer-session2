"""
this whole time we are using information that we have previously known in our application --> completely self-contained
but how do we get information to come into our application

one method is to get it from the user of our program (as text)
"""

"""
in order to get input from the user, we need a way to connect the keyboard of the user to our program

i want text --> we use a built-in function called input()
"""

# user_input = input("what do you wanna pass into the program? ")
# print(user_input)

"""
it is very critical to note that what the input function returns is always going to be a string. ALWAYS --> str
"""

# user_age = input("how old are you chief? ")

"""
but it doesnt make logical sense for us to get a string back from someone regarding their age
"""

# maturity_level = user_age - 69 # what will happen here?

"""
fix: cast whatever the input is to an int aka change the type from str to int
"""

str_user_age = input("seriously how old are you? ")
user_age = int(str_user_age) # youre at the mercy of the user

"""
OPTIONAL:
--> branching statement with an if - elif - else
        a bit more all over the place
        its better to take this route
--> exception / error handling will take care of it for you
        cleaner, better looking code 
        it is incredibly slow in terms of performance
"""

maturity_level = user_age - 69

print("this dudes age is", user_age)
print("his maturity level tho....", maturity_level)

