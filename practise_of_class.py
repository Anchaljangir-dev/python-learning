# problem one create a class(2-D vector) and use it to create another class of 3-D vector. 
class twoDvector:
    def __init__(self, i, j):
        self.i = i 
        self.j = j 
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")
class threeDvector(twoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k 
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")  

a = twoDvector(2, 3)
b = threeDvector(2, 3, 4)
a.show()
b.show()
# problem two create a class "pets" from class "animals" and further create a class "dogs" from class "pets". And a method "bark" to the class "dog"
class animals:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def show(self):
        print(f"The animal is {self.name} and it is a {self.species}")
class pets(animals):
    def __init__(self, name, species, owner):
        super().__init__(name, species)
        self.owner = owner
    def show(self):
        print(f"The pet is {self.name}, it is a {self.species} and its owner is {self.owner}")
class dogs(pets):
    def __init__(self, name, species, owner, breed):
        super().__init__(name, species, owner)
        self.breed = breed
    def bark(self):
        print(f"{self.name} is barking")
a = animals("leo", "lion")
b = pets("max", "dog", "john")
c = dogs("buddy", "dog", "jane", "labrador")
a.show()
b.show()
c.bark()
# problem 3 
class employee():
    salary = 205
    increments = 45
    @property
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increments/100))
    @salaryafterincrement.setter
    def salaryafterincrement(self, salary):
        self.increments = ((salary/self.salary) -1)*100

e = employee()
print(e.salaryafterincrement)
e.salaryafterincrement = 297.25
print(e.increments)

# problem 4 add complex numbers 
class complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i 
    def __add__(self, c2):
        return complex(self.r + c2.r, self.i + c2.i)
    def __str__(self):
        return f"{self.r} + {self.i}j"

c1 = complex(2, 3)
c2 = complex(4, 5)
print(c1 + c2)
# problem 6 adding and multiply a vector 
class vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
         result = vector(self.x + other.x, self.y + other.y, self.z + other.z)
         return result 

    def __mul__(self, other):
        result = (self.x * other.x + self.y * other.y + self.z * other.z)
        return result 

    def __str__(self):
        return f"vector({self.x}, {self.y}, {self.z})"


v1 = vector(3, 4, 5)
v2 = vector(9, 6, 7)
v3 = vector(9, 4, 2)

print(v1 + v2)
print(v1 * v2) 

# problem 7 len of a vector 
class vector:
    def __init__(self, l):
        self.l = l 

    def __len__(self):
        return len(self.l)

v = vector([1, 2, 4])
print(len(v))