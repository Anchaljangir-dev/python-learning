# finally must run in function even after return statement it used in functions 
def function():
    try:
        a = int(input("Enter a number: "))
        print(a)
        return
    except Exception as e:
        print(e)
        return

    finally:
        print("Hey I am inside finally")

function() # it normally runs but when we put return statement it also runs 
# in normal without function program finally runs in every condition and although we don put finally write only print it will also run 
# but in function when don write finally only write print it will not run 

# global key word we can change global variable by this 
a = 3
def fun():
    global a # its output will show 88 because of the global 
    a = 88
    print(a)

fun()
print(a) # here a is global variable if we use global key word we can change the value of a 

# enumerate using
l = [22, 33, 55, 66, 77, 88]
index = 0 
for item in l:
    print(f"The item number at index {index} is {item}")
    index+=1 # we can simplify this by using enumerate 

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")