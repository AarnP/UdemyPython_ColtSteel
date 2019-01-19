print("How many kilometers did you drive today?")
kms = input()  # Get input from the user and save value to the variable kms
print("Ok, you said " + kms)
miles = float(kms)/1.60934
# print(f"That is equal to {round(miles,2)} miles")

print("Your {} kilometers is equal to {} miles".format(kms, round(miles, 2)))

# round(thing to round, how many decimal points to round it to)
