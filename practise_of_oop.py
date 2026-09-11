# creating a class of programmer that stores few information of programmers of microsoft 
class programmers:
    company = "Microsoft" # class attribute

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary 
        self.pin = pin

p = programmers("Anchal", 120000, 341519)
print(p.name ,p.salary, p.pin, p.company, sep=" | ")
r = programmers("Rohan", 12000, 341520)
print(r.name, r.salary, r.pin, sep=" / ") # we can change objects like this but for same data we store in class like we store in company


# Make a calculator which calculates square cube and square roots using class and init
class calculator:
    def __init__(self , n):
        self.n = n 
    def square(self):
        print(f"The square of {self.n} is {self.n *self.n}")
    def cube(self):
        print(f"The CUBE of {self.n} is {self.n *self.n *self.n}")
    def squareroot(self):
        print(f"The square of {self.n} is {self.n**1/2}")
a = calculator(4)
a.square()
a.cube()
a.squareroot()



# instance attribute and class attribute 
class demo:
    a = 4
o = demo()
print(o.a) # prints the class attribute because instance attribute is not present 
o.a = 0 
print(o.a) # this is instance attribute  print the instnace attribute
print(demo.a) # prints class attribute 

# train booking problem through class 
from random import randint
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"Ticket is booked  in train no: {self.trainNo} {fro} to {to}")
    def status(self):
        print(f" Train no. {self.trainNo} is running on time {randint(1 , 12)} Pm onwards")
    def fare(self, fro, to ):
        print(f"fare of train no. {self.trainNo} from {fro} to {to} is {randint(250, 4456)}")
t = Train(10485)
t.book("Kuchaman" , "Delhi")
t.status()
t.fare("kuchaman", "Delhi")

# create a bank account management 
class bankaccount:
    name = "Anchal"
    pin = 341519
    balance = 40000
    def deposit(self, amount):
        self.amount = amount
        self.balance+=amount
        print(f"your amount of {self.amount} deposited successfully")
    def withdraw(self, amount):
        self.amount = amount
        
        if amount<=self.balance:
         self.balance-=amount
         print(f"your amount of {self.amount} has been withdrawed successfully")
        else:
            print("Insufficient amount to withdraw")
    def check_balance(self):
        print(f"your current balance is {self.balance} ")
    def change_pin(self, fro , to):
        old_pin = self.pin
        if self.pin ==fro:
            self.pin =to
            print(f"your pin from {old_pin} to {to} has been successfully changed")

        else:
            print("entered incorrect old pin: please try again!")
    
b = bankaccount()
b.deposit(3000)
b.withdraw(50000)
b.check_balance()
b.change_pin(341519, 341520)


class bankaccount:
    bank = "SBI"
    def __init__(self, name , balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin
        
    def deposit(self, amount):
        self.amount = amount
        self.balance+=amount
        print(f"Amount of {self.amount} has been deposited in {self.bank} successfully")
        print(f"And the current balance is {self.balance}")

    def withdraw(self, amount):
        self.amount = amount 
        if amount<=self.balance:
            self.balance-=amount
            print(f"amount of {self.amount} has been withdrawed successfully")
            print(f"And the current balance is {self.balance}")
        else:
            print("Insufficient bank balance")
    def change_pin(self, old_pin, new_pin):
            
            if self.pin ==old_pin:
                self.pin = new_pin
                print(f"pin has changed successfully from {old_pin} to {new_pin}")

            else:
                print(f"you entered wrong pin please try again!")
            



b = bankaccount("anchal", 50000,341519 ) 
b.deposit(40000)
b.change_pin( 341519, 341520)
c = bankaccount("Rohan", 40, 12)
c.deposit(50)
c.change_pin( 12, 14)
c.withdraw(30)