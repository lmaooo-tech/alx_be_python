"""
Develop a script named daily_reminder.py. This script will ask the user for a single task, its priority level, and if it is time-sensitive. The program will then provide a customized reminder for that task, demonstrating control flow and loops without relying on data structures to store multiple tasks.

Instructions:

Prompt for a Single Task:

Ask the user to input a task description and save it into a task variable
Prompt for the task’s priority (high, medium, low) and save it into a priority variable
In a time_bound variable, Ask if the task is time-bound (yes or no)
Process the Task Based on Priority and Time Sensitivity:

Use a Match Case statement to react differently based on the task’s priority.
Within the Match Case or after, use an if statement to modify the reminder if the task is time-bound.
Provide a Customized Reminder:

Print a reminder about the task that includes its priority level and whether immediate action is required based on time sensitivity.
A message should be ‘that requires immediate attention today!’
"""
#Ask for user input
task = str(input("Enter your task:"))
priority = str(input("Priority (high/medium/low):"))
time_bound = str(input("Is it time-bound? (yes/no):"))

#process the task based on priority and time
match priority:
	case "high":
		reminder = f"Task: {task} is a HIGH priority task"
	case "medium":
		reminder = f"Task: {task} is a MEDIUM priority task"
	case "low":
		reminder = f"Task: {task} is a LOW priority task"
	case _:
		reminder = f"Task: {task} has an unknown priority"

if time_bound.lower() == "yes":
	reminder += " that requires immediate attention today!"

print(reminder)