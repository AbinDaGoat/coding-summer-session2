"""
Write a program that asks the user for the value of a coin. Then determine
what kind of coin they entered using this information.

Sample runs:

Enter a coin value: 1
That's a penny!

Enter a coin value: 25
That's a quarter!

Enter a coin value: 99
That's not a valid coin!
"""

def main():
    print("sup")
    coin = int(input("what coin ya got? "))

    if coin == 1:
        print("homie got a penny")
    elif coin == 5:
        print("a nickel lulz")
    elif coin == 10:
        print("you a dime")
    elif coin == 25:
        print("a quarter it is")
    elif coin == 50:
        print("wow a whole half dollar")
    elif coin == 100:
        print("one dollahhhhhh")
    else:
        print("thats not valid!!! not very cash money of you")


main()




