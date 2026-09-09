# To make a simple calculator
# def cal():
#     sub = a - b
#     sum = a +b
#     multi = a*b 
#     choosefunction = input(("addition", "substraction", "multiply"))
#     if choosefunction == "addition":
#         return sum
#     if choosefunction =="substraction":
#         return sub
#     if choosefunction == "multiply":
#         return multi
# a = int(input("enter a number"))
# b = int(input("enter a number"))
# print(cal())
# To find which number is greatest using function 

def greatest(a, b, c, d):
    if (a>b or a>c or a>d):
        return a 
    elif (b>a or b>c or b>d):
        return b
    elif (c>a or c>b or c>d):
        return c
    elif (d>a or d>b or d>c):
        return d 
a =  int(input("enter a number"))
b =  int(input("enter a number"))
c =  int(input("enter a number"))
d =  int(input("enter a number"))

print(greatest(a , b, c , d))