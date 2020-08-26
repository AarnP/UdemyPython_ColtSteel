import requests
url = "https://icanhazdadjoke.com/search"
response = requests.get(
<<<<<<< HEAD
    url,
    headers={"Accept": "application/json"},
    params={"term": "cat", "limit": 1}
=======
                        url,
                        headers={"Accept": "application/json"},
                        params={"term": "cat", "limit": 1}
>>>>>>> 09d7747d4315c05c247dc796f95d13851849e9b1

)

data = response.json()

print(type(data))
print(data['results'])
# print(f"status:{data['status']}")
