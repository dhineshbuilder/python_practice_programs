line = input("Enter three numbers: ")
parts = line.split()

a = int(parts[0])
b = int(parts[1])
c = int(parts[2])

if a>b and a >c:
    print(f"{a} is largest")
elif b >a and b >c:
    print(f"{b} is largest")
else:
    print( f"{c} is largest")