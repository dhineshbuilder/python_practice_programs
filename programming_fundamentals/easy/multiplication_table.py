# Problem:
# Print the multiplication table of a number n from 1 to 10 in the format "n x i = result".

n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{i} x {n} = {i*n}")
