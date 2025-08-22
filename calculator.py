print("")
print("Welcome to the calculator created by Mikołaj.K")
print("")

print("Instructions:")
print("1: Enter the first number and press ENTER.")
print("2: Enter the second number and press ENTER again.")
print("3: Choose 1 of the 7 operators listed, type it, and press ENTER.")
print("4: The result will be displayed, then you can perform another operation.")
print("5: To exit the program, after the result is shown just press ENTER or close the window.")
print("")

while True:
    number_1 = float(input("number_1 : "))
    print("")
    number_2 = float(input("number_2 : "))
    print("")

    print("Type an operator: + addition, - subtraction, * multiplication, / division, // floor division, % modulus, ** power")
    print("")

    operator = input("operator : ")
    print("")

    if operator == "+":
        result = number_1 + number_2
    elif operator == "-":
        result = number_1 - number_2
    elif operator == "*":
        result = number_1 * number_2
    elif operator == "/":
        if number_2 == 0:
            result = "Error: division by zero"
        else:
            result = number_1 / number_2
    elif operator == "//":
        if number_2 == 0:
            result = "Error: division by zero"
        else:
            result = number_1 // number_2
    elif operator == "%":
        if number_2 == 0:
            result = "Error: division by zero"
        else:
            result = number_1 % number_2
    elif operator == "**":
        result = number_1 ** number_2
    else:
        result = "Error: invalid operator"

    print("The result is", result)
    print("")

    continue_program = input("Press Enter to exit or type anything to continue: ")
    if continue_program == "":
        break
