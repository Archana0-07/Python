# Program to check marks and display grade

marks=int(input("Enter marks:"))

if marks < 0 or marks > 100:
    print("invalid mark")
elif marks<35:
    print("Fail")
elif 35<=marks<50:
    print(" Pass - Grade C")
elif 50<=marks<70:
    print("Pass - Grade B")
elif 70<=marks<90:
    print("Pass - Grade A")
elif 90<=marks<=100:
    print("Pass - Grade O")





