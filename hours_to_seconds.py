"""
For this task, write a Python script that converts a specific number of hours into seconds. This task reinforces the concept of arithmetic operations within a practical context.

Instructions:

Create a file named hours_to_seconds.py.
Define a variable named hours and assign it a value representing the number of hours you want to convert to seconds. Use hours = 2.
Calculate the number of seconds in the given hours. Remember, there are 3600 seconds in an hour (since there are 60 minutes in an hour and 60 seconds in a minute, thus 60 x 60 = 3600).
Store the result of the conversion in a variable named seconds.
Print the result in the format: [hours] hour(s) is [seconds] seconds.
"""
#define the variables 
hours = 2 

#convert hours into seconds given 1hour=3600 seconds 
seconds = hours * 3600

#print the results 
print(f"{hours} hour(s) is {seconds} seconds")