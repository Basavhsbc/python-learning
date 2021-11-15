# In Python, an anonymous function is function without name and anonymous function are defined
# In Python, anonymous function are defined using keyword lamda and normal function are defined using keyword def
# To write lamda function in python,follow below syntax
## -- lambda arguments: expression
# Simple example of lamda function in python
double = lambda x : x*2
print(double(25))
# We use lambda function whenever we need nameless function for short period of time
# lambda function usually use in to evaluate  some expressions and it uses in higher large function
# Simple example to identify even items from below list and

my_list=[1,2,3,4,5,65,6,67,78,8,10,11]
new_list=list(filter(lambda x: (x%2 == 0), my_list))
new_double=list(map(lambda x: x*2, my_list))
print(new_double)

## To understand difference between normal function and lambda function in python
# Illustrating with cube function

def cube(x):
    return x*x*x

lambda_function= lambda y: y*y*y
# Using normal function
print(cube(5))
# Using lambda function
print(lambda_function(5))

# Without using Lambda: Here, both of them return the cube of a given number. But, while using def, we needed to define a function with a name cube and needed to pass a value to it. After execution, we also needed to return the result from where the function was called using the return keyword.
# Using Lambda: Lambda definition does not include a “return” statement, it always contains an expression that is returned. We can also put a lambda definition anywhere a function is expected, and we don’t have to assign it to a variable at all. This is the simplicity of lambda functions.

# def range_function():
#     for i in range(1,11):
#         print(i*2)

# tables=[lambda  x=x: x*10 for x in range(1,11)]
# for table in tables:
#     print(table())

Max= lambda a,b : a if a>b else b
print(Max(4,2))

func = lambda a,b : (a ** b)
print(func(float(10),20))

list1 = [3, 4, 5, 2, 1, 0]
print(list1.pop(0))