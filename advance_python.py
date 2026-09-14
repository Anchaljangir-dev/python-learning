# using walrus operator can do many operates by this 
if (n :=len([1, 2, 3, 4, 5])) > 3: # here we asing n equal to list and calculate the lenth of it
    print(f"length of list is too long {n} elements, expected <3")

# type definitions in python 
def sum (a: int, b: int) -> int: # it returns integer value 
    print(a + b)
sum(3, 5)

def show(a: str ,b: str) -> str:
    print(f"hello {a} your village is {b} ")

show("Anchal", "Chitawa")
from typing import List, Tuple, Dict, Union
numbers: List[int] = [1, 2, 3, 4, 5]
person: Tuple[str, int] = ("Anchal", 22)
scores: Dict[str, int] = {"Alice": 90, "Bob": 50}
identifier: Union[int, str] = "ID23fj" # we can use integer and string in this 
indentifier = 12234 # this is also valid 