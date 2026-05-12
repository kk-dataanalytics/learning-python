# Week 1 - Python Notes

## Variables and Strings

- Variables store data that can be referenced and reused throughout the program.
- Variable values can be reassigned and updated at any point in the code.
- String concatenation joins strings together using the + operator.

Escape characters allow special formatting inside strings:
- \n : creates a new line
- \" : allows quotes inside a string
- \\ : prints a backslash

String methods allow us to manipulate and inspect strings:
- .lower() : converts string to lower case
- .upper() : converts string to upper case
- .isupper() : returns True if string is uppercase
- .upper().isupper() : methods can be combined
- len() : returns the number of characters in a string
- [] : accesses a character by its index position
- .index() : finds the position of a character or substring
- .replace() : replaces part of a string with new text

## Numbers
- Python supports standard arithmetic operators: + - * / %
- % is the modulus operator and returns the remainder of a division.
- Brackets control the order of operations.
- str() converts a number to a string to allow concatenation with text.

Built-in number functions:
- abs() : returns the absolute value of a number
- pow() : raises a number to a power
- max() : returns the larger of two numbers
- min() : returns the smaller of two numbers
- round() : rounds to the nearest whole number

Math module functions (imported with from math import *):
- floor() : rounds a number down
- ceil() : rounds a number up
- sqrt() : returns the square root

## User Input
- input() captures what the user types and always returns it as a string.
- User responses are stored in variables for use later in the program.
- String concatenation is used to build the output message.

## Calculator
- input() is used to take two numbers from the user as strings.
- float() converts the strings to decimals to support numbers with decimal points.
- The converted values are added together and stored in a result variable.

## Mad Libs
- input() captures multiple user responses and stores them as strings.
- String concatenation joins the inputs into a sentence using the + operator.
- f-strings achieve the same result in a cleaner modern way by embedding 
variables directly inside the string using curly braces {}.