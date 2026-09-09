# correct_username = "Anchal"
# correct_password = 12345
# attempt = 0
# while attempt<3:
#     username = input("Enter the username: ")
#     password = input("Please enter your password: ")
#     if username ==correct_username or password ==correct_password:
#         print("you are successfully log in:")
#         break
#     else:
#         attempt+=1
#         if attempt<3:
#             print("wrong username or password try again!")
# else:
    # print(" too many wrong attempts login faild!")
# n = int(input("enter a number: "))
# for i in range(1 , n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")
# totalnumbers = 0 
# for n in range(2, 101):
#     is_prime = True
    

#     for i in range(2, n):
#         if n%i !=0:
#             is_prime = False
#             break

#     if is_prime:

        
#      print(n)
# n = int(input("enter numbers;"))
# a = 0
# b = 1
# i = 0
# numbers = []
# while i<n:
#     print(a)
#     a , b = b, a + b
#     i+=1
    
# write a fibonacci table 
n = int(input("enter numbers;"))
a = 0
b = 1
i = 0
numbers = []
while i<n:
    numbers.append(a)
    a , b = b, a + b
    i+=1

i = n-1
while i>=0:
    print(numbers[i])
    i -=1