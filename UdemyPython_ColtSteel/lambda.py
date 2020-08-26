# lambda num: num * num
# names = [
#     {'first': 'Rusty', 'last': 'Steel'},
#     {'first': 'Aaron', 'last': 'Rock'},
#     {'first': 'Dave', 'last': 'Van'}
# ]
#
# first_name = list(map(lambda x: x['first'], names))
# print(first_name)


# def decrement_list(aList):
#     return list(map(lambda x: x-1, aList))
#
#
# print(decrement_list([2, 3, 4]))


def remove_negatives(aList):
    return list(filter(lambda num: num >= 0, aList))


print(remove_negatives([1, -1, 2, -2, 3, -3]))
