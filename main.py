import requests
from mail import send_email

topic = "cricket"
api_key = "fcb0f287b9af4b698812a5172e49bb9d"
url = "https://newsapi.org/v2/everything?"\
    f"q={topic}"\
    "&from=2024-12-01"\
    "&sortBy=publishedAt"\
    "&apiKey=fcb0f287b9af4b698812a5172e49bb9d"\
    "&language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][0:20]:
    title = article["title"] if article["title"] is not None else "No Title"
    description = article["description"] if article["description"] is not None else "No Description"
    url = article["url"] if article["url"] is not None else "No URL"
    body = "Subject:Today's news" + "\n" + body + article["title"] + "\n" \
           + article["description"] \
           + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
