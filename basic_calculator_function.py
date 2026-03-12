def my_function():
    num_1=int(input("enter your first number="))
    num_2=int(input("enter your second number="))
    add=num_1+num_2
    print("addition=",add)
    sub=num_1-num_2
    print("subtraction",sub)
    mul=num_1*num_2
    print("multiplication",mul)
    div=num_1/num_2
    print("division",div)

    if num_1==num_2:
        print("equal")
    else:
        print("not equal")

my_function()
