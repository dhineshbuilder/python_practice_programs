# Problem:
# Swap two variables a and b WITHOUT using a third variable.
# Show two different ways:
# 1) Python-specific method (Tuple unpacking)
# 2) Arithmetic method (Addition & Subtraction)

a = 10
b = 9

print(f"Initial values: a={a}, b={b}")

a,b = b,a

print(f"After tuple unpacking method: a={a}, b={b}")

print(f"Before arthematic swaping method: a={a}, b={b}")

a = a+b
b = a -b
a = a - b

print(f"After arthematic swaping method: a={a}, b={b}")