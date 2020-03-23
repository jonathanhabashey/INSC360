# Author: Jonathan Habashey
# Date: 03/23/2020
# Description: This homework contains 2 programs, one where I concatenate two stringd via a function
# and one that uses a class and makes an instance of my pet and then prints out a statement
# using a function inside of my class

# Class initialization
class Pet:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species
    # Function to print once class is filled with info needed
    def display_info(self):
        print("I have a {} named {} who is {} years old".format(self.species, self.name, self.age))


# Funciton to merge two stringd
def merge_strings(str1, str2):
    str3 = str1 + " " + str2
    print(str3)


string1 = input("Please Enter your first string: ")
string2 = input("Please enter your second string: ")

merge_strings(string1, string2)

print("\n")

# Puts info into class, then prints it using function in class
my_pet = Pet("Caesar", 5, "dog")
my_pet.display_info()

