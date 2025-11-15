"""
Assign specific values to two variables, number1 and number2.
Perform addition, subtraction, and multiplication on these numbers.
Print the results of these operations in a human-readable format.
Instructions:

Create a file named basic_operations.py.
In this file, you will define two variables: number1 and number2, with the values 10 and 5, respectively.
You do not need to write any functions or import any modules.
Calculate the sum, difference (by subtracting number2 from number1), and product of number1 and number2.
Print the results of each operation in the format: [operation] of [number1] and [number2] is [result].
"""
#Defining variables 
number1 = 10
number2 = 5

#Forming addition expression
sum = number1 + number2
difference = number1 - number2 
product = number1 * number2 

# print results 
print(f"Addition of {number1} and {number2} is {sum}")
print(f"Subtraction of {number1} and {number2} is {difference} ")
print(f"Multiplication of {number1} and {number2} is {product}")