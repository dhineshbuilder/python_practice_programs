line = input("Enter two numbers and an operator (e.g. 10 / 5):")
parts = line.split()

num1 = float(parts[0])
op = parts[1]
num2 = float(parts[2])

if op not in ['+','-','*','/']:
    print(f"Error: invalid operator'{op}'")

elif op == '/' and num2 ==0:
    print("Error: division by zero")

elif op == '+':
    print(num1 + num2)

elif op == '-':
    print(num1 - num2)

elif op == '*':
    print(num1 * num2)

elif op == '/':
    print(num1 / num2)

