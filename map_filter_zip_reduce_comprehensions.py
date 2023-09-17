# map

# def multiplyBy3(value):
#     return value * 2


# res = list(map(multiplyBy3, [4, 8, 7]))
# print(res)


# def power(v):
#     return v ** 2


# res1 = tuple(map(power, [2, 3, 5]))
# print(res1)


# filter
# def is_eligible(value):
#     return value >= 18


# is_eligible = list(filter(is_eligible, [18, 2, 37, 17, 21]))
# print(is_eligible)

# zip

# my_list = [1, 4, 5, 6]
# your_list = [4, 7, 8, 9]
# res = list(zip(my_list, your_list))
# print(res)


# reduce

# from functools import reduce


# def sum0fAll(accumulator, item):
#     return accumulator+item


# res = reduce(sum0fAll, [1, 2, 3, 4], 10)
# print(res)

# my_strings = ['a', 'b', 'c', 'd']
# my_numbers = [4, 3, 2, 1]

# res = list(zip(my_strings, my_numbers))
# print(sorted(res))

# x = 'kdp'

# print(x.capitalize())

# 1 Capitalize all of the pet names and print the list
# my_pets = ['sisi', 'bibi', 'titi', 'carla']


# def captializeValue(value):
#     return value.upper()


# res = list(map(captializeValue, my_pets))
# print(res)


# Lambda functions

# from functools import reduce


# my_list = [1, 2, 3, 4, 5]

# # multiply by 2
# x = list(map(lambda x: x*2, my_list))
# print(x)

# # filter odd

# y = list(filter(lambda x: x % 2 != 0, my_list))
# print(y)

# # Multiply all the elements
# z = reduce(lambda acc, item: acc*item, my_list)
# print(z)

# # square the list

# res = list(map(lambda y: y**2, my_list))
# print(res)

# list- sorting

# x = [(1, 9), (4, 2), (2, 4), (6, 9), (1, 5), (-2, 4)]

# x.sort(key=lambda x: x[1])
# print(x)


# my_dict = {x: x*2 for x in [1, 2, 3]}
# print(my_dict)

#  find the duplicates
# some_lists = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# duplicates = list({x for x in some_lists if some_lists.count(x) > 1})
# print(duplicates)
