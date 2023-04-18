# Exercise 10 - News App Solution & Shoutout | Python Tutorial - Day #93

# https://www.youtube.com/watch?v=bnAz7Kb2efE&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=93


import requests
import json

query = input("What type of news are you interested in?: ")
url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-03-18&sortBy=publishedAt&apiKey=API_KEY"

r = requests.get(url)
# print(r.text)

news = json.loads(r.text)

for article in news["article"]:
    print(article["title"])
    print(article["description"])
    print("-----------------------------------------")