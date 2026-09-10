# class employee:
    
#     language = "Python"
#     salary = 120000 

# anc = employee()
# anc.name = "Anchal"
# print(anc.name, anc.language, anc.salary)
'''salary and language are class attributes 
and name is a instance attribute
Instance attribute takes prefrence over class attribute'''
class employee:
    
    language = "Python"
    salary = 120000 

    def getinfo(self):
     print(f"the language is {self.language} and the salary is {self.salary}")
anc = employee()
anc.getinfo() # we can use function like this but we have to give self parameter 
# @staticmethod is a decorater method because of this we dont need object we dont need any property 