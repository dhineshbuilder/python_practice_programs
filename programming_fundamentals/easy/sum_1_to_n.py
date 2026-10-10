# Problem:
# Compute the sum of numbers from 1 to n using:
# 1) a loop
# 2) a mathematical formula
# Print both results and check if they match.

n = int(input("Enter a number: "))

#sum using a loop

loop_sum = 0

for i in range(1,n+1):
    loop_sum += i

print(f"Loop sum = {loop_sum}")

#sum using gaussian formula

formula_sum = n * (n+1) // 2

print(f"formula sum = {formula_sum}")

match = (loop_sum == formula_sum) 

print(f"match = {match}")
