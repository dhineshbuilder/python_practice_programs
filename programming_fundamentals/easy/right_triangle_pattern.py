# Problem:
# Print a right-angled triangle of '*' with n rows.
# Each row should contain the row number of stars.

n = int(input("Enter a number: "))

for i in range(1,n+1):
    for j in range(i):
        print("*",end="")
    print()

for i in range(1,n+1):
    print("*"*i)