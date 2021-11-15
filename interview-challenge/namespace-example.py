# x= 'global'
# def f():
#     x='enclosed'
#     def g():
#         x='local'
#         print(locals())
#         print(x)
#     g()
# # To call function in python
# f()

def f():
      s = 'foo'
      x = 20
      loc = locals()
      print(loc)
      loc['s'] = 'bar'
      print(s)
f()