age = 21
# 2 - 8: $2 ticket
# 65: $5 ticket
# Other people: $10 ticket

if not ((age >= 2 and age <= 8) or age >= 65):
    print("You PAY 10 dollars and are not a child or senior!")
else:
    print("You are a child or senior!")
