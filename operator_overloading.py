class Number:
    def __init__(self, n):
        self.n = n 
    def __add__(self, other): # here other is another object of class Number and we are overloading the + operator 
        return self.n + other.n 
M = Number(5) # this is object of class Number 
N = Number(10) # this is object of class Number 
print(N + M) # this prints 15 because we have overloaded the + operator
# there are multiple overloading methods __sub__ , __mul__ , __truediv__ , __floordiv__ , __mod__ , __pow__ , __lt__ , __le__
