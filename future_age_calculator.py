"""
Create a Python script that asks the user for their current age and then calculates how old they will be in a specific future year. This task introduces handling user input and reinforces arithmetic operations.

Instructions:

Create a file named future_age_calculator.py.
Prompt the user to input their current age with the question: “How old are you? ”.
Assume the user will input a valid integer value.
Calculate how old the user will be in the year 2050. To keep calculations simple, assume the current year is 2023. Therefore, you need to add 27 years to the user’s current age.
Print the user’s age in 2050 in the format: In 2050, you will be [age] years old.

"""
#prompt the user for the current age 
current_age = int(input( "how old are you?"))
age_in_2050 = current_age + 27  #since 2050 - 2023 =27

#print results 
print(f"In 2050, you will be {age_in_2050} years old")
