from importlib.resources import contents

import requests

api_key = "fcb0f287b9af4b698812a5172e49bb9d"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-12-01&sortBy=publishedAt&apiKey=fcb0f287b9af4b698812a5172e49bb9d"

request = requests.get(url)
content = request.json()

for articles in content["articles"]:
    print(articles["title"])
    print(articles["content"])
