# myList = [1, 2, 3, 5, 6, 7]
# squaredList = []
# for item in myList:
#     squaredList.append(item*item)

# print(squaredList) # we dan do this work in shorter method using list comprehension method 

# squaredList = [ i*i for i in myList]
# print(squaredList) 

# creating table using list comprehension in a file
n = int(input("Enter a number: "))
table = [n*i for i in range(1, 11)]
with open("tables.txt", "a") as f:
    f.write(f"The table of {n} is: {str(table)} \n")
