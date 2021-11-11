# def fruits():
#     return ["apple","mango"]
#
# my_dict={"name": "basav", "things": fruits()}
# # To print dictionary
# print(my_dict)
#
# bagpack = {"Books": 5, "Camera": 1, "Fruits": {"Apple": 1, "Orange": 2}}
# print(bagpack["Fruits"]["Orange"])
# mydict = {"name": "Shantanu", "age": 20, "grades": "A", "age": 22}
# print(mydict)
# mydict1 = {"name": "Shantanu", 21: "age", False: "Palash", (1,2): "numbers"}
# print(mydict1)
# def name():
#     pass
# my_dict={name(): "Siddayya", False: "Palash"}
# print(my_dict[name()])

# def fruits():
#     return ["apple","lemon"]
# my_dict={"name": "basavraj nilkanthe","age":32,"things": fruits()}
# print(my_dict["things"])
# print(my_dict["name"])
# fav_list = {"colors": ["Skyblue", "grey"], "number": 21, "fruits": ["Orange", "Mango", "Blueberries"]}
# print(fav_list["fruits"][:2])
# numbers={"num1": 23,"num2": 12}
# numbers["num1"]=13
# numbers["num3"]=10
# print(numbers.items())
# print(type(numbers.items()))
# print(list(numbers.items())[0])
numbers = { "num1": 10, "num2": 13, "num3": 23}
# for k,v in numbers.items():
#     print(k,v)
# print(list(numbers.keys()))
# ##########
# for key in numbers.keys():
#     print(numbers[key])
#
# ######
# print(list(numbers.values()))
# print(numbers.get("num4"))
# numbers.update({"num2": 5, "num4": 10})
# print(numbers.clear())
print(numbers.pop("num5",00))
print(numbers.popitem())