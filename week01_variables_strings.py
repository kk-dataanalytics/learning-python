"""
Week 1 - Variables and Strings
Practice based on FreeCodeCamp Python tutorial
Concepts: variables, strings concatenation, escape characters, string methods
"""

# Variables and data types
character_age = "28"
character_name = "Jessica"

# Using variables in strings
print("There once was a women named " + character_name + ",")
print("she was " + character_age + " years old.")

# Changing variable value
character_name = "Charlotte"
print("But she really liked the name " + character_name + ",")
print("and she didn't like being " + character_age+ ".")

# Working with strings

# New line
print("Giraffe\nAcademy")

# Escape character (quotes inside string)
print("Giraffe\"Academy")

# Backslash
print("Giraffe\\Academy")

phrase = "Giraffe Academy"

# Concatenation
print(phrase + " is educational")

# String methods
print(phrase.lower())   # convert to lower case
print(phrase.upper())   # convert to upper case
print(phrase.isupper()) # returns True if string is uppercase
print(phrase.upper().isupper())  # combining methods

# String length
print(len(phrase))

# Access character by index
print(phrase[0])

# Finding character index
print(phrase.index("A"))
print(phrase.index("Acad"))

# Replace text
print(phrase.replace("Giraffe", "Lion"))
