# range is sequence of numbers
for i in range(4):
    print(i) # it default take 0 to starting range print until n-1 

# step size is a function through it we can print numbers by adding manual gaps
for i in range(1 , 100, 4):
    print(i) # here 4 is number which it skip and 1 is starting range and 100 is ending range 


# we can use forloop in list tuple string contant 
l = [1, 2, 4, 5, 6, 7, 8, 46543, 33423, 243,24]
for i in l:
    print(i)


list = ["Anchal", "Is", "A", "good", "Girl"]
for i in list:
    print(i) # it will print this list one by one
# to print a string characters
string = "Anchal"
for i in string:
    print(i)

# for loop with else
L1 = [1, 4, 6]
for item in L1:
    print(item)
else:
    print("Done:")

# the break statement exit the loop right now 
for i in range(100):
    if i ==34:
        break
    print(i)

# continue statement
for i in range(100):
    if i ==34:
        continue
    print(i) # it skips iteration 344 

# pass statement null statement in python it instruct to do nothing 
