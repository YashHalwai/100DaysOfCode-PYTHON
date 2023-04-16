# Requests Module in Python | Python Tutorial - Day #89

# https://www.youtube.com/watch?v=Nsb3bLIlO4w&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=89


import requests

# response = requests.get("https://www.codewithharry.com")

# print(response)
# print(response.text)



url = "https://jsonplaceholder.typeicode.com/posts"

data = {
    "title" : "harry",
    "body" : "bhai",
    "userId" : 12,
}

headers = {
    'Content-type' : 'application/json; charset = UTF-8',
}

response = requests.post(url, headers = headers, json = data)


# print(response.text)

# BeautifulSoup => html.parser