"""
define a fully-functioning program (with a main function) that asks for the user's name, age, and favorite food
and responds with a greeting that includes their name, age, and fav food

example output:
"Hello Mo! I would imagine that I also like escargot at the age of 26!"

"""


def get_user_name():
    name = input("whats your name? ")
    return name
    # return input("whats your name? ")


def get_user_age():
    # str_age = input("how old are you? ")
    # age = int(str_age)
    age = int(input("how old are you? "))
    return age


def get_user_fav_food():
    fav_food = input("what food do you like to eat bruh? ")
    return fav_food


def main():
    print("Hello, I have a few questions for you:")
    name = get_user_name()
    age = get_user_age()
    fav_food = get_user_fav_food()
    print("Well", name, ", I would imagine that I also like", fav_food, "at the age of", age)


main()
