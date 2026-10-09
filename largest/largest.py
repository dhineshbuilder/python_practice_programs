line = input("Enter three numbers:")
parts = line.split()

a = int(parts[0])
b = int(parts[1])
c = int(parts[2])

best = a

if b > best:
    best=b

if c > best:
    best=c

print(best)