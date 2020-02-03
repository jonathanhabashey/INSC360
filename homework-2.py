# Author: Jonathan Habashey
# Date: 01/27/2020
# Filename: homework-2.py
# Description: Messes with strings using functions we learned in class

string_1 = "This is a test string."
string_2 = "This is also a test string."
string_3 = "Knock Knock!\nWho's there?\nOrange!\nOrange who?\nOrange you glad I didnt say \"banana!?\""
number_string = "1234"

print(string_1, string_2, string_3, number_string)

print("\n")

joined_string = string_1 + " " + string_2

print(joined_string)

print("\n")

print(string_3.replace("\"banana!?\"", "\"grapes!?\"", 1))

print("\n")

new_numbers = int(number_string)

print(new_numbers)
