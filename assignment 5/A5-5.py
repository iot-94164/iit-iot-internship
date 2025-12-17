from operations import arithmetic
from operations import strings_ops

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", arithmetic.add(a, b))
print("Multiplication:", arithmetic.mul(a, b))

text = input("Enter a string: ")

print("Reversed String:", strings_ops.reverse_string(text))
print("Number of vowels:", strings_ops.count_vowels(text))