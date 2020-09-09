calculator = "calc"
print(calculator.upper())

while True:
    num1 = float(input("first number: "))
    op = input("Operator: ")
    num2 = float(input("second number: "))

    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2)
    else:
        print("invalid operator!!!")

    q = input("Do you want to continue? y/n: ")
    if q == "y":
        continue
    elif q == "n":
        break
    else:
        print("invalid argument!!!!")
        break
