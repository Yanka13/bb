import requests


def quote()
  url = "https://wagon-breaking-bad-quotes.herokuapp.com/v1/quotes"
  call = requests.get(url)
  response = call.json()[0]
  return (f"{response['author']} says : {response['quote']}")
