'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''

# Function exercise 49


# def list_manipulation(list, command, location, val=None):
#     if command == 'remove':
#         if location == 'beginning':
#             remov_elem = list.pop(0)
#             print(remov_elem)
#             return remov_elem
#         if location == 'end':
#             remov_elem = list.pop()
#             print(remov_elem)
#             return remov_elem
#     if command == 'add':
#         if location == 'beginning':
#             list.insert(0, val)
#             print(list)
#             return list
#         if location == 'end':
#             list.append(val)
#             print(list)
#             return list
#
#
# list_manipulation([1, 2, 3], 'remove', 'beginning')


# Function exercise 50
# def is_palindrome(a):
#     if a == a[::-1]:
#         print("It is a palindromew")
#         return True
#     else:
#         print("It is not a palindromew")
#         return False
#
#
# is_palindrome("testing")


'''
frequency([1,2,3,4,4,4], 4) # 3
frequency([True, False, True, True], False) # 1
'''


# def frequency(aList, val):
#     if val in aList:
#         count = aList.count(val)
#         print(count)
#         return count
#
#
# frequency([1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4], 4)


# def frequency(aList, val):
#     for val in aList:
#         count = aList.count(val)
#         print(count)
#         return count


# '''
# multiply_even_numbers([2,3,4,5,6]) # 48
# '''
#
#
# def multiply_even_numbers(aList):
#     result = 1
#     for num in aList:
#         if num % 2 == 0:
#             result = result * num
#     print(result)
#     return result
# multiply_even_numbers([2, 3, 4, 5, 6])


# def evens_product(xs):
#     product = 1
#     for i in xs:
#         if i % 2 == 0:
#             product *= i
#     print(product)
#     return product
# evens_product([2, 3, 4, 5, 6])


'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''


# def capitalize(aList):
#     a = aList[0:1].upper()
#     b = aList[1::1]
#     ans = a + b
#     print(ans)
#     return(ans)
# capitalize("Tim")


'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''


# def compact(aList):
#     a = []
#     for check in aList:
#         if check:
#             a.append(check)
#     print(a)
#     return a
# compact([0, 1, 2, "", [], False, {}, None, "All done"])

# flesh out intersection pleaseeeee
# def intersection(listA, listB):
#     ans = []
#     for check in listA and listB:
#         if check in listA and listB:
#             ans.append(check)
#     print(ans)
#     return ans

# intersection([1, 2, 3], [2, 3, 4])


'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''


# def partition(aList, callFunctn):
#     firstList = []
#     secondList = []
#     finalList = []
#     for check in aList:
#         if callFunctn(check):
#             firstList.append(check)
#         else:
#             secondList.append(check)
#     finalList = [firstList, secondList]
#     print(firstList)
#     print(secondList)
#     print(finalList)
#     return finalList
#
#
# def isEven(num):
#     return num % 2 == 0
#
#
# partition([1, 2, 3, 4], isEven)


'''
calculate(make_float=False, operation='add', message='You just added', first=2,
second=4) # "You just added 6"
calculate(make_float=True, operation='divide', first=3.5, second=5)
# "The result is 0.7"
'''


# def calculate(**kwargs):
#     operation_lookup = {
#         'add': kwargs.get('first', 0) + kwargs.get("second", 0),
#         'subtract': kwargs.get('first', 0) + kwargs.get('second', 0),
#         'multiply': kwargs.get('first', 0) * kwargs.get('second', 0),
#         'divide': kwargs.get('first', 0) / kwargs.get('second', 1)
#     }
#     is_float = kwargs.get('make_float', False)
#     operation_value = operation_lookup[kwargs.get('operation', '')]
#     # kwargs.get('operation') to get the value of the required operation and then
#     # access that individual value inside dictionary operation_lookup by using syntax
#     # operation_lookup['key_name']
#     if is_float:
#         final = "{} {}".format(kwargs.get('message', 'The result is'),
#                                float(operation_value))
#     else:
#         final = "{} {}".format(kwargs.get('message', 'The result is'),
#                                int(operation_value))
#     print(final)
#     return final
#     # operation_value = operation_lookup[kwargs.get('operation', '')]
#
#
# calculate(make_float=False, operation='add', message='You just added', first=2,
#           second=4)


def test_kwargs(mark1, mark2):
    print(mark1, mark2)


people = {'mark1': 20, 'mark2': 19}


test_kwargs(**people)
