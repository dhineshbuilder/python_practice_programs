# Problem:
# Given a mark (0-100), convert it to a grade using the following rules:
#     >= 90     : A
#     >= 75     : B
#     >= 60     : C
#     >= 40     : D
#     otherwise : F

mark = int(input("Enter your mark: "))

if mark < 0 and mark >100:
    print("Invalid")
elif mark>=90:
    print("A grade")
elif mark>=75:
    print("B grade")
elif mark>=60:
    print("C grade")
elif mark >=40:
    print("D grade")
else:
    print("F grade")
