num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
match_case = input("Choose the operation (+, -, *, /): ")
if match_case == "+":
    result = num1 + num2
    print(f"The result is: {result}")
elif match_case == "-":
    result = num1 - num2
    print(f"The result is: {result}")
elif match_case == "*":
    result = num1 * num2
    print(f"The result is: {result}")
elif match_case == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result is: {result}")
    else:
        print("Cannot divide by zero.")