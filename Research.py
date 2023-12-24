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




#--------------------------------------------------------#



# TODO: how_do_i_create_a_function_in_python:

name = 'oriel'
def greet_someone(names):
print(names)

greet_someone(name)



def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b:

'''
# docstring

 - *—@@—- Concept: docstring —-@@—*
        idea: - A docstring is the word for word example of what the functions purpose is and what its doing
'''


'''
Things to consider below $$$


In Python, indentation is used to indicate blocks of code, including the body of functions. The use of colons (:) at the end of function definitions, conditional statements, loops, etc., signals the start of an indented block. The indentation level determines the scope of the code.

In contrast to JavaScript, where curly braces {} define blocks of code and semicolons ; terminate statements, Python relies on consistent indentation to define the structure of the code. This is known as the "off-side rule" and is a distinctive feature of Python's syntax.


For example, in JavaScript:
function myFunction() {
  // This is the scope of the function
let x = 10;
if (x > 5) {
    // This is the scope of the if statement
    console.log("x is greater than 5");
} else {
    // This is the else block
    console.log("x is not greater than 5");
}
  // End of the function scope
}





In Python, the equivalent code would be:
def my_function():
    # This is the scope of the function
    x = 10
    if x > 5:
        # This is the scope of the if statement
        print("x is greater than 5")
    else:
        # This is the else block
        print("x is not greater than 5")
    # End of the function scope

'''

#--------------------------------------------------------#
# how_do_i_create_a_’string’_in_python
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




'''
All subjects researched and completed! wonderful

Sample functions and normal problems solved in python below
'''

# Addition Function:
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


# Factorial Function:
def factorial(n):
    """Returns the factorial of a non-negative integer."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# List Reversal Function:
def reverse_list(input_list):
    """Returns the reversed version of a list."""
    return list(reversed(input_list))


# Palindrome Checker Function:
def is_palindrome(word):
    """Checks if a word is a palindrome."""
    cleaned_word = ''.join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]


# Temperature Converter Function:
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32


# Outputs for the functions above:
result = add_numbers(3, 5)
print(result)

fact_result = factorial(4)
print(fact_result)

reverse_result = reverse_list([1, 2, 3, 4, 5])
print(reverse_result)

palindrome_check = is_palindrome("A man, a plan, a canal, Panama!")
print(palindrome_check)

temp_conversion = celsius_to_fahrenheit(25)
print(temp_conversion)
