n = int(input("enter a number:"))
for i in range(1,11):
    print(f"{n} X {i} = {n * i}")
# method to make a mathematical table 
# to greet special name in a list 
List1 = ["Ram", "Shyam", "Radhe", "surya", "saurabh"]
for name in List1:
    if(name.startswith("s")):
        print(f"Hello {name}")

n = int(input("enter a number:"))
i = 1
while i<11:
    print(f"{n} X {i} = {n*i}")
    i +=1 # solving problem 1 by using while loop

# to check a number which is prime or not 
# a prime number is which devide by itsef or one 
n = int(input("enter a number:"))
for i in range(2,n):
    if (n%i) ==0:
        print("This is not a prime number")
        break
else:
    print("this is a prime number")
# sum of first natural numbers
n = int(input("enter a number:"))
i = 1
sum = 0
while i<=n:
    sum+=i
    i +=1

print(sum)

# factorial by using for loop
n = int(input("enter a number:"))
product = 1
for i in range (1, n+1):
    product = product*i
print(f"Factorial of {n} is {product}")


# make stars for n lines 
n = int(input("enter the number:"))
for i in range(1, n+1):
    print(" "* (n-i), end="")
    print("*"* (2*i-1), end="")
    print("")

n = int(input("enter the number:"))
for i in range(1,n+1):
    if i ==1 or i ==n:
        print("*"*n, end="")

    else:
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")

# write a program to multiply a table in reverse order
n = int(input("enter a number"))
for i in range(1, 11):
    print(f"{n} X {11 - i} = {n} * {11-i}") 
# count all prime numbers upto 100
totalnumbers = 0 
for n in range(2,101):
    is_prime = True
    for i in range(2,n):
        if n%i==0:
            is_prime = False

        if is_prime:
         totalnumbers+=1
print(totalnumbers)