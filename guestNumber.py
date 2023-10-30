print("\n-----------------------WELCOME TO SHORT FORM GENERATOR------------------\n")

import random

def guess_number(x):
    hidden_number = random.randint(1,x)

    your_input = 0
    while your_input != hidden_number:
        your_input = int(input("Enter your guest number : "))

        if your_input < hidden_number:
            print("Too low. Try again.")
        if your_input > hidden_number:
            print("Too high. Try again.")

    print("\n\nCongratulation! You win.")
    print("\n\n-----------------------THANK YOU USE ME---------------------")
guess_number(10)