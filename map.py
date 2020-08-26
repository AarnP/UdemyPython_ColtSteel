nums = [2, 4, 6, 8, 10]

doubles = map(lambda x: x*2, nums)

for num in doubles:
    print(num)
    
people = ["Darcy", "Christina", "Dana", "Annabel"]

peeps = map(lambda name: name.upper(), people)
upper_name = list(peeps)
print(upper_name)

num_list = [8, 9, 10]
decrement_list = map(lambda x: x-1, num_list)

for number in decrement_list:
    print(number)