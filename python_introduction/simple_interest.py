"""
Your task is to complete a Python script that calculates the simple interest earned on an investment over a period of time. The formula for simple interest is (I = P * R * T), where:

( I ) is the interest earned,
( P ) is the principal amount (initial investment),
( R ) is the annual interest rate (as a decimal),
( T ) is the time the money is invested for in years.
Instructions:

Create a file named simple_interest.py.
Define three variables in this file:
principal with a value of 1000 (representing $1000),
rate with a value of 0.05 (representing 5% annual interest rate),
time with a value of 3 (representing 3 years).
Calculate the simple interest using the formula provided and store the result in a variable named interest.
Print the calculated interest in a format: The simple interest is: [interest].
"""
#define the variables
principal  = 1000  #represents 1000$
rate  = 0.05 #representing 5% annual interest rate
time  = 3 #representing 3 years 

#calculate the simple interest
interest =  principal * rate  * time


#print results 
print(f"The simple interest is:", {interest})