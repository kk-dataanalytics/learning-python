"""
 Week 1 - Mad libs game
 Practice based on FreeCodeCamp Python tutorial
 Concepts: input(), string concatenation, f-strings
"""

# User input stored as strings
colour = input(" Enter a colour: ")
plural_noun = input(" Enter a plural noun: ")
flower = input(" Enter a flower: ")

# result printed using string concatenation
print("Roses are " + colour)
print(plural_noun + " are blue")
print("I adore " + flower)


# same result using f-strings (modern approach)
print(f"Roses are {colour}")
print(f"{plural_noun} are blue")
print(f"I adore {flower}")
