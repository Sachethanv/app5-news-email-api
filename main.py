import requests
from mail import send_email

# News API Configuration
topic = "cricket"
api_key = "fcb0f287b9af4b698812a5172e49bb9d"
url = (
    "https://newsapi.org/v2/everything?"
    f"q={topic}"
    "&from=2024-12-01"
    "&sortBy=publishedAt"
    "&apiKey=fcb0f287b9af4b698812a5172e49bb9d"
    "&language=en"
)

# Fetch news articles
request = requests.get(url)
content = request.json()

# Prepare the email content
body = ""
for article in content["articles"][:20]:
    title = article["title"] if article["title"] else "No Title"
    description = article["description"] if article["description"] else "No Description"
    url = article["url"] if article["url"] else "No URL"
    body += f"{title}\n{description}\n{url}\n\n"

# Send the email
send_email(message=body)
