for x in range(1, 21):
    if x == 4 or x == 13:
        state = "unlucky"
    elif x % 2 == 0:
        state = "even"
    else:
        state = "odd"
    print("{} is {}".format(x, state))
    # print(f"{num} is {state}")
