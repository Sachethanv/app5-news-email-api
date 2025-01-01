     import smtplib
import ssl
from email.mime.text import MIMEText

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "sachethanv.codes@gmail.com"
    password = "enxi ldta qniw wevi"
    receiver = "aj062209@gmail.com"

    # Create an email message with utf-8 encoding
    msg = MIMEText(message, "plain", "utf-8")
    msg["From"] = username
    msg["To"] = receiver
    msg["Subject"] = "Today's News"

    # Create a secure SSL context
    context = ssl.create_default_context()

    # Connect to the SMTP server and send the email
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())

