# from random import random
#
#
# def flip_coin():
#     # Generate random number 0 - 1
#     r = random()
#     if r > 0.5:
#         return "Heads"
#     else:
#         return "Tails"
#
#
# print(flip_coin())


def generate_evens():
    result = []
    for num in range(1, 50):
        if num % 2 == 0:
            result.append(num)
            print(result)
    return result


generate_evens()
