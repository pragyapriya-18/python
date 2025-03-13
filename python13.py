####program to illustrate exeption handling####
a=int(input("enter value of a"))
b=int(input("enter value of b"))
try:
    if b==0:
         raise ArithmeticError
    else:
        print("a/b=", a/b)
except ArithmeticError as e:
    print(e)