# Ask for a joke, software return:
# - Multiple result: pick one random (use random module)
# - 1 result: print that result
# - No joke: Sorry, no joke, please try again
#
# Stage:
# - Ask users for input
# - Send request to search endpoint
# - query string term whatever user TypeErro
# - Use if condition
from random import choice
import requests

user_input = input("Let me tell you a joke! Give me a topic: ")

url = "https://icanhazdadjoke.com/search"
response = requests.get(url,
                        headers={"Accept": "application/json"},
                        params={"term": user_input}
                        ).json()
# Print number of joke
num_joke = response["total_jokes"]
results = response["results"]
if num_joke > 1:
    print(f"I found {num_joke} about {user_input}. Here's one: ")
    print(choice(results)['joke'])
elif num_joke == 1:
    print(f"I found {num_joke} about {user_input}. Here's one: ")
    print(results[0]['joke'])
else:
    print(f"Sorry, couldn't find a joke with your term: {user_input}")
