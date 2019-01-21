# ask for age
# age = input("How old are you: ")
# if age != "":  # Check if the user enter the age value or not
#     age = int(age)
#     if age >= 18 and age < 21:
#         print("You can enter but need a wristband")
# # 18 - 21 wristband
# # 21+ drink, normal entry
#     elif age >= 21:
#         print("You are good to enter and can drink!")
# # too young, sorry
#     else:
#         print("You can't come in, little one!")
# else:
#     print("Please enter your age!!")

age = input("How old are you: ")
if age:  # Check if the user enter the age value or not
    age = int(age)
    if age >= 21:
        print("You are good to enter and can drink!")

    elif age >= 18:
        print("You are good to enter and can drink!")
# too young, sorry
    else:
        print("You can't come in, little one!")
else:
    print("Please enter your age!!")
