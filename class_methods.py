# python give preference to instance attribute but if we want to print class atribute we can use @classmethod 
class employee:
    a = 1
    def show(cls):
        print(f"the class attribute is {cls.a}")

o = employee()
o.a = 45
o.show() # this is shows 45 because the object attribute is given preference over class attribute 
# but if we want class attribute
class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"the class attribute is {cls.a}")

o = employee()
o.a = 45
o.show()  # this prints 1  
