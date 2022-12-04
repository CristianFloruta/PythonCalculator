from art import logo

def add(num1, num2):
    return num1 + num2


def substract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def calculator(num1, num2, operation_symbol):
    return operations[operation_symbol](num1, num2)


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

calculation_on = True

print(logo)


num1 = float(input("What is your first number?"))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operations from the line above: ")

num2 = float(input("What is your second number?"))

first_result = calculator(num1, num2, operation_symbol)

print(f"{num1} {operation_symbol} {num2} = {first_result}")

use_result = input(
    f"Whould you like to use the {first_result} for other operations? Type 'y' for yes or 'n' for no: ").lower()

while calculation_on:

    operation_symbol = input("Pick an operations from the line above: ")

    num2 = float(input("What is your next number?"))

    result = calculator(num1, num2, operation_symbol)

    print(f"{num1} {operation_symbol} {num2} = {result}")

    if input(
            f"Whould you like to use the {result} for other operations? Type 'y' for yes or 'n' for no: ").lower() == 'y':
        num1 = result

    else:
        calculation_on = False

