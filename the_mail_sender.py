# Importing libraries and twilio-python important stuff
import os
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
from dotenv import load_dotenv
from twilio.rest import Client

# Loading .env file 
load_dotenv()

# Setting up local variables
sendgrid_api_key = os.getenv("SENDGRID_API_KEY")
verified_sender = os.getenv("SENDGRID_VERIFIED_SENDER")
receiver = os.getenv("EMAIL_RECEIVER")
email_subject = "Nerd alert, nerd alert! I used python to send you this."

# Writing my bs message bellow
content = Content(
    "text/plain", 
    '''
        Hi! My name is Eric, i'm a CNU nerd! Come join my nerdy troop at mojo dojo casa house, CNU, Virginia!

        Tentativa número 112379812 de integrar a API do twilio sendgrid no python, agoravaicaralho.txt.

        Só receba meu belo código anexado em png, beijos, liebe Grüße, xoxo
    '''
)

# Setting up mail info
sg = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key)
from_email = Email(verified_sender)
to_email = To(receiver)
mail = Mail(from_email, to_email, email_subject, content)

# Getting json formatted mail
mail_json = mail.get()

# Finally, sending the mail
# Send an HTTP POST request to /mail/send
response = sg.client.mail.send.post(request_body=mail_json)

# Regular python debug stuff
print(response.status_code)
print(response.headers)


