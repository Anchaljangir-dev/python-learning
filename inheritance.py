# to make multiple classes 
class employee:
    company = "ITC"
    def show (self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")


class programmer:
    company = "MICROSOFT"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

    def language(self):
        print(f"the language of employee is {self.language}")

a = employee()
b = programmer()
print(a.company, b.company)

# usually we can do this same work by inheritence instead of much more lines of code like this : as same data of employee
# and when we have to do change we can only change in employee class and extra information we can print like this 
class employee:  # this is the base class or parent class 
    company = "ITC"
    name = "Anchal"
    salary = 12000
    def show (self):
        
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class programmer(employee): # this is the derived class or inheritance class 
    company = "MICROSOFT"
    language = "python"
    def language(self):
        
        print(f"the language of employee is {self.language}")
a = employee()
b = programmer()
print(a.company, b.company)
print(a.show())
print(b.show())

# multilevel inheritence 
class employee:
    a = 1
class coder(employee):
    b = 2 
class manager (coder):
    c = 3

o = employee()
print(o.a)
x = coder()
print(x.a, x.b)
y = manager 
print(y.a, y.b, y.c)


# super method use to print parental constructor 
class employee:
    def __init__(self):
        print("constructor of employee")
    a = 1
class coder(employee):
    def __init__(self):
            print("constructor of coder")
    b = 2 
class manager (coder):
    def __init__(self):
            print("constructor of manager ")
    c = 3

# o = employee()
# print(o.a)
x = coder()
print(x.a, x.b)
# y = manager 
# print(y.a, y.b, y.c)
# this plays one by one we can play the parental constructor by using super method 
class employee:
    def __init__(self):
        print("constructor of employee")
    a = 1
class coder(employee):
    def __init__(self):
            print("constructor of coder")

    b = 2 
class manager (coder):
    def __init__(self):
            super().__init__()
            print("constructor of manager ")
    c = 3

# o = employee()
# print(o.a)
x = coder()
print(x.a, x.b)
# y = manager 
# print(y.a, y.b, y.c)