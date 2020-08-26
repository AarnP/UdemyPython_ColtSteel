import random
number = 0
i = 0
while number != 5:
    i += 1
    number = random.randint(1, 10)
    print("i: {}, number: {}".format(i, number))
    if number == 5:
        break
