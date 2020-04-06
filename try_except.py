try:
    user_input = int(input("Enter a number: "))
    print(user_input)
except ValueError as ve:
    print(ve)
except ArithmeticError:
    print("")