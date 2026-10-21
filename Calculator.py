import os
os.system('cls')
total = float(input("enter the first number:"))
while True:
    operator = input("Enter operator:")
    if operator == "exit":
        break
    number = float(input("Enter the number:"))
    if operator == "+":
        total = total + number
    elif operator == "-":
        total = total - number
    elif operator == "*":
        total = total * number
    elif operator == "/":
        if number == 0:
            print("you can't divide by zero")
        else:
            total = total / number
    else:
        print("Wrong operator")
    print(total)
print(total)
