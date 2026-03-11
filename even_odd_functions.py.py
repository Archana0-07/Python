 #function without parameter
def fun():
    num=int(input("Enter a number:"))
    if num%2==0:
        print("even")
    else:
        print("odd")
fun()


#function with parameter
def fun2(num1):
    if num1%2==0:
        print("even")
    else:
        print("odd")
fun2(20)
fun2(3)
fun2(16)
fun2(33)


#function with multiple arguments
def fun3(*nums):
    for num in nums:
        if num%2==0:
            print(num,"even")
        else:
            print(num,"odd")
fun3(1,2,3,4,5,6)


#function with normal and variable arguments
def fun4(msg,*nums):
    for num in nums:
        if num%2==0:
            print(msg,"even")
        else:
            print(msg,"odd")
fun4("this is",5,6,7,3)

