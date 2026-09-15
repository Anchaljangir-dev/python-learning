from functools import reduce 
# create a table of 7 by list comprehension and write down it verticle in string 
table = [str(7*i) for i in range(1, 11)]
s = "\n".join(table)
print(s) 

# creating a list number which only divisible by 5 
def devisible5(n):
    if (n%5 ==0):
        return True
    return False


a = [2343, 54353, 255, 5555, 535, 34535, 56535, 2423, 2425, 53563, 43435]

f = list(filter(devisible5, a))
print(f)

# find the greatest number in a list 
l = [2343, 54353, 255, 5555, 535, 34535, 56535, 2423, 2425, 53563, 43435]
def greatest(a, b):
    if a>b:
        return a
    return b
print(reduce(greatest, l)) # for this we have to import reduce from functools module 

