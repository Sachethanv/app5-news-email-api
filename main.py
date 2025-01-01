import requests
from mail import send_email



api_key = "fcb0f287b9af4b698812a5172e49bb9d"
url = "https://newsapi.org/v2/everything?q=tesla&from=2024-12-01&sortBy=publishedAt&apiKey=fcb0f287b9af4b698812a5172e49bb9d"

request = requests.get(url)
content = request.json()


body =""
for articles in content["articles"]:
    body = body + articles["title"] + "\n" + articles["description"]+2*"\n"



body = body.encode("utf-8")
send_email(message=body)
