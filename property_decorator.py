class employee:
    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = employee()
e.name = "John Doe"
print(e.name) # this prints John Doe
print(e.fname, e.lname) # this prints John Doe 