import requests
import json

query = input(" What is the news you want ? ")
url = f"https://newsapi.org/v2/everything?q={query}&from=2023-06-13&sortBy=publishedAt&apiKey=7f086535a42e4fac8923c664c665017d"
r = requests.get(url)
news = json.loads(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("_________________")
