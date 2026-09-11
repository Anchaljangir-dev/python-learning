#_init_constructor 
class employee:
    language = "python" # this is class attribute 
    salary = 1200000
    def __init__(self): # This is called dunder method in python 
        print("I am creating a object") # this did not need to be called 
    @staticmethod
    def greet(): # this did not need self 
        print("hello anchal")

    def getInfo(self):
        print(f"My salary is {self.salary} and language is {self.language}")
anc = employee()
anc.name = "Anchal"
