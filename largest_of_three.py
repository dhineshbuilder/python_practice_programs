# Problem:
# Find the largest of three numbers without using the max() function.

parts = input("Enter three number to find largest: ").split()

a = int(parts[0])
b = int(parts[1])
c = int(parts[2])

if a>=b and a >=c:
    print(f"{a} is the largest numbers")
elif b>=c:
    print(f"{b} is the largest numbers")
else:
    print(f"{c} is the largest")