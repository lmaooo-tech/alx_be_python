"""
Create a Python script named multiplication_table.py. This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.

Instructions:

Prompt User for a Number:

Ask the user to input a number for which they want to see the multiplication table: Enter a number to see its multiplication table:.
Save it in a variable name number
Generate and Print the Multiplication Table:

Use a for loop to iterate through the numbers 1 to 10.
For each iteration, calculate the product of the user’s number and the iterator (the current number in the loop from 1 to 10).
Print each line of the multiplication table in the format: “X * Y = Z”, where X is the user’s number, Y is the current number in the loop, and Z is the product.
"""
#Prompt the user for a number

number = int(input("Enter a number to see its multiplication table:"))
for i in range(1,11):
 # The variable 'i' will take on values 1, 2, 3, ..., 10
  print("\nMultiplication table for {number}:\n")
for i in range(1, 11):
 print(f"{number} * {i} =  {number * i}")