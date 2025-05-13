import requests

response = requests.get('https://v2.jokeapi.dev/joke/Any')

print(response.status_code)  # Should print 200 if the request was successful
joke_dictionary = response.json()
print(joke_dictionary["type"])
print(joke_dictionary["setup"])  