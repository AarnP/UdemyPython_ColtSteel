# q1 = [1, 2, 3, 4]
# q2 = [3, 4, 5, 6]
# a1 = [num for num in q1 if num == 3 or num == 4]
# a2 = [num for num in q2 if num == 3 or num == 4]
# answer = [num for num in q1 and q2 if num == 3 or num == 4]
# print(answer)

# q3 = ["Elie", "Tim", "Matt"]
# answer2 = [char[::-1].lower() for char in q3]
# print(answer2)

# answer = [num for num in list(range(1, 101)) if num % 12 == 0]

answer = [char for char in 'amazing' if char not in 'aeiou']
print(answer)
