# languages = ['Java', 'Python', 'JavaScript']
# versions = [14, 3, 6]
# result=zip(languages)
# print(list(result))
#
# number_list = [1, 2, 3]
# str_list = ['one', 'two', 'three']
#
# # No iterables are passed
# result = zip()
#
# # Converting iterator to list
# result_list = list(result)
# print(result_list)
#
# # Two iterables are passed
# result = zip(number_list, str_list)
#
# # Converting iterator to set
# result_set = set(result)
# print(result_set)
# Different number of iterable
numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

list1 = ['s', 'r', 'a', 's']
list2 = ['a', 'a', 'n', 'h']
["".join([i, j]) for i, j in zip(list1, list2)]