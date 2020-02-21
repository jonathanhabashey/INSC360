# Author: Jonathan Habashey
# Date: 02/24/2020
# Description: Program generates a random number then the user gets to guess the number
# it also makes sure the number is between 1 and 10 and that it is a number.
import random
print('*'*56)
random_num = random.randint(1,10)
print("* A random number between 1 and 10 has been generated.” +\  “ Can you guess what it is?”)")
entry = input("Enter a number: ")
run = "yes"

# While loop to run all the checks with the condition starting off as true
while run == "yes":

    while not entry.isnumeric():
        entry = input("That is not a number! Please enter only a number: ")


    entry = int(entry)


    while entry < 1 or entry > 10:
        entry = input("Please enter a number between 1 and 10: ")
        entry = int(entry)

    # Once number is guessed while loop condition is changed and the program is exited
    if entry == random_num:
        print("You win, congratulations!")
        run = "no"

    if entry > random_num:
        print("entry is too big!")


    if entry < random_num:
        print("entry is too small!")
        
    # Asks the user to input another number if they guessed incorrectly
    if run == "yes":
        entry = input("Enter another number: ")




