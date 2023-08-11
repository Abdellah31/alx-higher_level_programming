#!/usr/bin/python3
a = 10
b = 5
from calculator_1 import add, subtract, multiply, divide

sum_result = add(a, b)
diff_result = subtract(a, b)
prod_result = multiply(a, b)
div_result = divide(a, b)

print("Addition: {} + {} = {}".format(a, b, sum_result))
print("Subtraction: {} - {} = {}".format(a, b, diff_result))
print("Multiplication: {} * {} = {}".format(a, b, prod_result))
print("Division: {} / {} = {}".format(a, b, div_result))
