# student = {
#     "name": "Aaron",
#     "owns_dog": False,
#     "num_courses": 1,
#     "favourite_language": "Python, C",
#     "is_hillarious": True,
#     13: "my favourite number!"
# }

# artist = {
#     "first": "Neil",
#     "last": "Young",
# }
#
# full_name = artist['first'] + " " + artist['last']
#
# print(full_name)

# donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)
# # DON'T TOUCH PLEASE!
# for v in donations.values():
#     total_donations += v
#     print(total_donations)

# from random import choice
# food = choice(["cheese pizza", "quiche", "morning bun", "gummy bear", "tea cake"])

# bakery_stock = {
#     "almond croissant": 12,
#     "toffee cookie": 3,
#     "morning bun": 1,
#     "chocolate chunk cookie": 9,
#     "tea cake": 25
# }

# YOUR CODE GOES BELOW:
# if food in bakery_stock.keys():
#     print("{} left".format(bakery_stock[food]))
# else:
#     print("We don't make that")

inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}  # DON'T CHANGE THIS LINE!

# Make a copy of inventory and save it to a variable called stock_list USE A DICTIONARY METHOD
stock_list = {}
stock_list.update(inventory)
# print(stock_list)
# add the value 18 to stock_list under the key "cookie"
new_stock = dict(cookie=18)
stock_list.update(new_stock)

# remove 'cake' from stock_list USE A DICTIONARY METHOD
stock_list.pop('cake')
print(stock_list)
