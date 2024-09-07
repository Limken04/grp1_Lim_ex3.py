# Filename: grp1_Lim_ex3.py

# 1. Calculate the length of a string
string = "I am Programmer, I have no life.!"
length_of_string = len(string)
print("Length of 'I am Programmer, I have no life.!':", length_of_string)

# 2. Count the number of characters in a string
char_count = len(string)
print("Number of characters in 'I am Programmer, I have no life.!':", char_count)

# 3. Replace all occurrences of the first character with '$', except the first character itself
def replace_first_char(string):
    first_char = string[0]
    modified_string = first_char + string[1:].replace(first_char, '$')
    return modified_string

# Example with the string "banana"
string_to_modify = "banana"
print("String after replacing first char occurrences:", replace_first_char(string_to_modify))

# Example with the string "success"
string_to_modify = "success"
print("String after replacing first char occurrences:", replace_first_char(string_to_modify))

# 4. Swap the first two characters of two strings and concatenate them
def swap_first_two_chars(string1, string2):
    swapped_string1 = string2[:2] + string1[2:]
    swapped_string2 = string1[:2] + string2[2:]
    return swapped_string1 + " " + swapped_string2

string1 = "I Am"
string2 = "Programer"
result = swap_first_two_chars(string1, string2)
print("Swapped and concatenated:", result)

# 5. Concatenate five variables with spaces
var1 = "Python"
var2 = "is"
var3 = "a"
var4 = "language"
concatenated_string = var1 + " " + var2 + " " + var3 + " " + var4
print("Concatenated strings:", concatenated_string)

# 6. Concatenate two user input strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
concatenated_input_string = string1 + " " + string2
print("User concatenated strings:", concatenated_input_string)

# 7. Concatenate your name and age in a paragraph
name = "Alvinson "
age = 22
paragraph = "My name is " + name + " and I am " + str(age) + " years old."
print(paragraph)