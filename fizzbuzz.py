# Problem:
# Print numbers from 1 to n.
# - For multiples of 3, print "Fizz".
# - For multiples of 5, print "Buzz".
# - For multiples of both 3 and 5, print "FizzBuzz".
# - Otherwise, print the number itself.

number = int(input("Enter a number for fizzbuzz: "))

for i in range(1, number+1):
    if i%3==0 and i%5==0:
        print("Fizzbuzz")
    elif i%3 ==0:
        print("Fizz")
    elif i%5 ==0:
        print("Buzz")
    else:
        print(i)
