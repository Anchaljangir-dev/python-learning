# Function has to be called 
def avg(): # function definition
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))
    c = int(input("Enter a number: "))
    d = int(input("Enter a number: "))
    average = (a + b + c + d)/4
    print(average)
    return "Ok thanks"
A = avg() 
print(A) 

 
# def greet():
#     print("Have a good day Anchal")
# greet()


# two type of function 
#builtin function 
#userdefined function 
# Function with arguments
# def greet(name, ending):
#     print("Good day " + name + ending)

# greet("Anchal", "Thankyou")
# Return is a function which ask to give a value to function 
def greet(name, ending):
    print("Good day " + name + ending)
    return "OK"

a = greet("Anchal", "Thankyou")
print(a) 
# Recursion 
def factorial(n):
    if n==0 or n==1:
        return 1 
    return n *factorial(n-1)
n = int(input("enter a number: " ))
print (f"factorial of {n} is : {factorial(n)}")


