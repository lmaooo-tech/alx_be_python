# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'

    Returns:
        float or str: Result of the arithmetic operation, or an error message for division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "ERROR_DIV_ZERO"
        return num1 / num2
    else:
        return "INVALID_OPERATION"("Invalid operator. Use one of '+', '-', '*', '/'.")

		
