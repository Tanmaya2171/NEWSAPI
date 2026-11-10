import requests

query = input("What types of news are you intrested ?")
api = "8d6e6907309b4d3094698f4f21c8b2e1"

url = f"https://newsapi.org/v2/everything?q={query}&from=2026-10-10&sortBy=publishedAt&apiKey={api}"

print(url)
r = requests.get(url)
data = r.json()

articles = data["articles"]

for index, article in enumerate(articles):
    print(index + 1, article["title"],article["url"])
    print("\n************************\n")