# if we want to square a number of any mathemetical operation we simple does this 
""" def square(i):
        return i*i
        return i+i
    square(4)
    """ 
# but using lamda function 
square = lambda x:x*x
print(square(5))
sum = lambda a, b, c: a+b+c
print(sum(5, 6, 4))

# join method 
L = ["Anchal", "Jangid", "software_developer", "Foreign"] # use to join string 
jointL = "::".join(L)
print(jointL)


# format method in former version before f string use to use it
a = "{1} is a good {0}".format("Anchal", "girl") # output: girl is a good anchal 
print(a) # we can also index it 