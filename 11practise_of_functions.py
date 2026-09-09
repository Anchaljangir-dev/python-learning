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

# def greatest(a, b, c, d):
#     if (a>b or a>c or a>d):
#         return a 
#     elif (b>a or b>c or b>d):
#         return b
#     elif (c>a or c>b or c>d):
#         return c
#     elif (d>a or d>b or d>c):
#         return d 
# a =  int(input("enter a number"))
# b =  int(input("enter a number"))
# c =  int(input("enter a number"))
# d =  int(input("enter a number"))

# print(greatest(a , b, c , d))
# def fun():
#     C = int(input("enter the temperature "))
#     return (C * 9/5) +32
# a = fun()
# print(round(a, 2) ,"F")
# end ="" to prevent a new line 
# def sum(n):
#     if n ==1:
#         return 1
#     return sum(n-1) + n 

# print(sum(4))

# # print reverse star pattern 
# def pattern(n):
#     if n ==0:
#         return
#     print("*" *n)
#     pattern(n-1)
# pattern(8)
# write a program to change inches to centimeters 
# def inch_to_cen(inches):
#     return inches*2.54
# n = int(input("enter the value in inches: "))
# print(f"The corresponding value in cms i : {inch_to_cen(n)}")
def rem(l, word):
    n = []
    for item in l:
        if not(item ==word):
            n.append(item.strip(word))
    return n 
l = ["anchal", "herry", "potter", "al"]
print(rem(l , "al"))
# to strip and remove a character and a word on same time 