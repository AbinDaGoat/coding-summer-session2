"""
write a fully-functioning program (with a main function) that gets the user's name and age
if they are above the age of 18, they get drafted into the army
if they are or below the age of 18, they stay in school
NOTE: if the user gives an invalid age, make sure to print out a warning message
"""


def get_name_and_age():
    name = input("whats your name bruh? ")
    age = int(input("how old are ya? "))
    return name, age


def main():
    print("hi welcome to this weird program!!!")
    name, age = get_name_and_age()
    if age > 18:
        print("hey", name, "straight to the army for you!")
    elif 0 < age and age <= 18:
    # elif 0 < age <= 18: # only a thing in python
        print("so", name, "you need to stay in school because its cool")
    else:
        print(name, "are you a real human? thats not a real age!!!")


main()

