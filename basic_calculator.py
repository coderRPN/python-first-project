operator = input("Enter operator: ")
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "/":
    print(first / second)
elif operator == "*":
    print(first * second)
else:
    print("Invalid operator")
