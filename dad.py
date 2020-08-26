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
import random
import requests
import json

tell_joke = input("Let me tell you a joke! Give me a topic: ")
url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url,
    headers={"Accept": "text/plain"},
    params={"term": tell_joke, "lim": 1}

)
# Get data into dictionary
# data = response.json()
# # Access data in list
# data_in_list = data['results']
# # Turn joke variable into a dictionary
# joke = {}
# for joke in data_in_list:
#     print(joke['joke'])
# print(type(joke))
# def make_joke():
#     if response
data = response.text
print(data)
