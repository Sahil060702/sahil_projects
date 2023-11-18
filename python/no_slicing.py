#find the reverse of a string without using slicing and reverse method.
def reverse_string(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Example usage
input_str = input("Enter a string: ")
result_str = reverse_string(input_str)
print("Reversed String:", result_str)
