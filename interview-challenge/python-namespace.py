a=2
print('id(a)=',id(a))
print('id(2)=',id(2))
a=a+1
print('id(a)=',id(a))
print('id(3)=',id(3))
b = 2
print('id(b) =', id(b))
print('id(2) =', id(2))
################ *********################

def outer_function():
    global a
    a=20
    def inner_function():
        global a
        a=30
        print("a=",a)
    inner_function()
    print("a=",a)
a=10
outer_function()
print("a=",a)
# var1 is in the global namespace
var1 = 5

################
def some_func():
    # var2 is in the local namespace
    var2 = 6
    def some_inner_func():
        # var3 is in the nested local
        # namespace
        var3 = 7
        print("var3=", var3)
    some_inner_func()
some_func()
######
count=5
def some_method():
    global count
    count=count+1
    print(count)
some_method()

# Python3 code to demonstrate dir()
# when no parameters are passed

# Note that we have not imported any modules
print(dir())

# Now let's import two modules
import random
import math

# return the module names added to
# the local namespace including all
# the existing ones as before
print(dir())
# Python program showing
# a scope of object
######
def some_func():
    print("Inside some_func")
    global var
    var=var+1
    def some_inner_func():
        #var = 10
        print("Inside inner function, value of var:", var)
    some_inner_func()
    print("Try printing var from outer function: ", var)
var=55
some_func()

# Python3 code to demonstrate dir()
# when no parameters are passed

# Note that we have not imported any modules
print(dir())

# Now let's import two modules
import random
import math

# return the module names added to
# the local namespace including all
# the existing ones as before
str="siddayya"
print(dir())

# Python3 code to demonstrate dir() function
# when a module Object is passed as parameter.

# import the random module
import random

# Prints list which contains names of
# attributes in random function
print("The contents of the random library are::")

# module Object is passed as parameter
print(dir(random))