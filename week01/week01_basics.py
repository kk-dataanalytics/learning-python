"""
Week 1 - Python Basics
Practice based on FreeCodeCamp Python tutorial
Concepts: variables, strings, numbers, math module, user input
"""

# Variables and data types

character_age = "28"
character_name = "Jessica"
print("There once was a women named " + character_name + " ,")
print("she was " + character_age + " years old.")

character_name = "Charlotte"
print("But she really liked the name " + character_name + ",")
print("and didn't like being " + character_age + ".")

# working with strings

print("Giraffe\nAcademy")
print("Giraffe\"Academy")
print("Giraffe\\Academy")

phrase = "Giraffe Academy"
print(phrase + " is educational")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("A"))
print(phrase.index("Acad"))
print(phrase.replace("Giraffe", "Lion"))

# working with numbers

print(-2.098)
print(3 + 4.5)
print(3 / 6)
print(8 * 4)
print(10 % 3)
print(3 * 4 + 5)
print(3 * (4 + 5))

print(-2.098)
print(3 + 4.5)
print(3 / 6)
print(8 * 4)
print(10 % 3)
print(3 * 4 + 5)
print(3 * (4 + 5))


my_num = -21
print(abs(my_num))

print(pow(3, 2))
print(max(6, 8))
print(min(6, 8))
print(round(3.6))

from math import *

print(floor(4.7))
print(ceil(4.7))
print(sqrt(36))

# getting input from users

name = input("Enter your name:")
age = input("Enter your age: ")
print(" Hello " + name + " ! You are " + age)

# building a basic calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result)

# mad libs game

colour = input(" Enter a colour: ")
plural_noun = input(" Enter a plural noun: ")
flower = input(" Enter a flower: ")

print("Roses are " + colour)
print(plural_noun + " are blue")
print("i adore " + flower)
