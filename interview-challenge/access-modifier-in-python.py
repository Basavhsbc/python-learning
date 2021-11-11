## To access class attributes publicly in python and which is similar to public keyword
## In python it has different way of defining access modifier in python
## To define public attribute, refer below example
# class Modifiers:
#     def __init__(self,name):
#         self.public_member=name
#
# mod = Modifiers("Nihar")
# mod.public_member="Nihar Nilkanthe"
# print(mod.public_member)

# Protected Access Modifier behavior with single under_score
# However, this doesn’t fully perform the functionality of the protected modifier.
# The attribute defined in the above program is accessible outside the class scope. It can also be modified as well.
# class Modifiers:
#     def __init__(self,name):
#         self._public_member=name
#
# mod = Modifiers("Nihar")
# mod._public_member="Nihar Nilkanthe"
# print(mod._public_member)

# Private Access Modifier behavior with double under_score
class Modifiers:
    def __init__(self,name):
        self.__public_member=name

mod = Modifiers("Nihar")
# mod.__public_member="Nihar Nilkanthe"
print(mod.__public_member)

