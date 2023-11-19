#Write a program to segregate a number from a string.
import re

def segregate_numbers(input_string):
    # Use regular expression to find all numbers in the string
    numbers = re.findall(r'\d+', input_string)
    
    
    # Convert the numbers from strings to integers
    numbers = list(map(int, numbers))
    
    return numbers

# Example usage:
input_string=input("enter a string with number:")
result = segregate_numbers(input_string)
print(result)
