# Problem:
# Read two numbers and an operator (+, -, *, /). Print the result.
# If the operator is invalid or you divide by zero, print a clear error message.

inputs = input("Enter two numbers and an operator(eg : 10 / 5): ")
parts = inputs.split()

num1 = float(parts[0])
op = parts[1]
num2 = float(parts[2])

if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == "*":
    print(num1*num2)
elif op == "/":
    if num2 == 0:
        print("Error : divison by zero")
    else:
        print(num1 / num2)
else:
    print("Error: invalid operator")