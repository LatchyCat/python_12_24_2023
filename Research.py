'''
     - *—@@—- Concept: —-@@—*
        idea: -
        boil_down_point: -
'''

'''
    - # Single-Line Comments: # This is a single-line comment

# x = 10  # This is an inline comment explaining the variable assignment


    - Multi-Line Comments:
In Python, there is no explicit syntax for multi-line comments, but you can use triple-quotes
(3 xQuotes' or """) to create a string literal, which can serve as a multi-line comment.
The interpreter will ignore these strings, treating them as comments.
'''

    # TODO: how_do_i_create_an_object{}_in_python 
# Define a class
class Dog:
    # Class variable
    species = "Canis familiaris"

    # Constructor method (initializer)
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print(f"{self.name} says Woof!")

# Create an object (instance) of the Dog class
my_dog = Dog(name="Buddy", age=3)

# Accessing object attributes
print(f"{my_dog.name} is {my_dog.age} years old.")
print(f"{my_dog.name} belongs to the species {my_dog.species}.")

# Calling an object method
my_dog.bark()




    # TODO: how_do_i_create_a_function_in_python








#--------------------------------------------------------#
#how_do_i_create_a_’string’_in_python
# Creating a f string
    print(f'hello this is a f type string or string interpellation like in javaScript')
    print ('Make sure to use brackets to capsulate the variable, function, or operator being used to properly use interpellation')

# ---@@-- Using f-strings (formatted string literals) --@@---
name = "John"
age = 30

# f-string
sentence = f"My name is {name} and I am {age} years old."
print(sentence) #Output: My name is John and I am 30 years old.



# ---@@-- Using the str.format() method: --@@---
name = "Jane"
age = 25

# format method
sentence = "My name is {} and I am {} years old.".format(name, age)
print(sentence) #Output: My name is Jane and I am 25 years old.



# ---@@-- Using the % operator (similar to C-style formatting): --@@---
name = "Bob"
age = 40

# % operator
sentence = "My name is %s and I am %d years old." % (name, age)
print(sentence) #Output: My name is Bob and I am 40 years old.

