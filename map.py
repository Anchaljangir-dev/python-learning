from functools import reduce
# example of map 
l = [1, 2, 3, 5, 6]
square = lambda x: x*x
sqlist = map(square, l)
print(list(sqlist))

# Filter example
def even(n):
    if (n%2) ==0:
        return True
    return False
onlyeven = filter(even, l)
print(list(onlyeven))

# reduce example
def sum(a, b):
    return a + b
print(reduce(sum , l))
def mul(a, b):
    return a*b
print(reduce(mul, l))