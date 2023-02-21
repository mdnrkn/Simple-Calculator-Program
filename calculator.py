# prompt the user for input
operator = input("Enter an operator (+, -, *, /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# perform the calculation based on the operator
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: division by zero")
        exit()
    result = num1 / num2
else:
    print(f"Error: {operator} is not a valid operator")
    exit()

# format and print the result
formatted_result = "{:,.2f}".format(result)
print(f"The result is: {formatted_result}")
