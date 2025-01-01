import smtplib
import ssl


def send_email(message):#function takes one argument, message, which is the content of the email you want to send (both subject and body).
    host =  "smtp.gmail.com" #This is the SMTP server of Gmail, "smtp.gmail.com"
    port=465 #This is the port number used for SMTP over SSL
    username = "sachethanv.codes@gmail.com"#his is the sender’s email address, i.e., the email account you are using to send the email. Here, it’s "sachethanv.codes@gmail.com"
    password = "enxi ldta qniw wevi"
    receiver = "sachethanv.codes@gmail.com"#This is the recipient’s email address. In this case, it’s the same as the sender (you are sending the email to yourself: "sachethanv.codes@gmail.com")
    context = ssl.create_default_context()#This creates a secure SSL context, which is necessary for encrypting the connection when you connect to the SMTP server using SSL (port 465).


    with smtplib.SMTP_SSL(host, port , context = context ) as  server:
        #This line establishes a secure connection to Gmail’s SMTP server using the SSL context on port 465.
        server.login(username , password)
        #This line logs into the Gmail account using the provided username (email) and password (or app password).

        server.sendmail(username, receiver , message)
        #This sends the email from the sender (username) to the recipient (receiver) with the content defined in message.
