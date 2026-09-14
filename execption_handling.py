# a = int(input("hey, enter a number: "))
# print(a) # prgrammer failure when enter the name anchal to fix this 
try:
    a = int(input("hey, enter a number: "))
    print(a)
except Exception as e:
    print(e)   # this method will print error and not show error 


# raising value error like zerodivision error 
a = int(input("enter a number: "))
b = int(input("enter a number: "))
if b ==0:
    raise ZeroDivisionError("hey our program is not meant to be devide by zero")
else:
    print(f"The devision of {a} and {b} is {a/b}")

# try and else if try block successfully runs it goes into else 
try:
 a = int(input("enter a number: "))
except ValueError as e:
   print(e)
else:
   print("i am inside else")
