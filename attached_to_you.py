# Importing libraries and twilio-python important stuff
import base64
import os
from dotenv import load_dotenv
import sendgrid
from sendgrid.helpers.mail import (
    Mail, Attachment, FileContent, FileName,
    FileType, Disposition, ContentId, Content, Email, To)
from sendgrid import SendGridAPIClient

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

        Só receba meu belo código anexado como attached_to_you.py, beijos, liebe Grüße, xoxo
    '''
)

from_email = Email(verified_sender)
to_email = To(receiver)
mail = Mail(from_email, to_email, email_subject, content)

# Setting up the message
message = Mail(
    from_email=from_email,
    to_emails=to_email,
    subject=email_subject,
    html_content=content
    )

# Setting up attachment file
file_path = 'attached_to_you.py'
with open(file_path, 'rb') as f:
    data = f.read()
    f.close()
encoded = base64.b64encode(data).decode()
attachment = Attachment()
attachment.file_content = FileContent(encoded)
attachment.file_type = FileType('application/pdf')
attachment.file_name = FileName(file_path)
attachment.disposition = Disposition('attachment')
attachment.content_id = ContentId('Extreme noise terror Content ID')
message.attachment = attachment

# Setting up mail info
sg = sendgrid.SendGridAPIClient(api_key=sendgrid_api_key)

# Getting json formatted mail
mail_json = mail.get()

# Finally, sending the mail
# Send an HTTP POST request to /mail/send
sendgrid_client = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
response = sendgrid_client.send(message)

# Regular python debug stuff
print(response.status_code)
print(response.headers)
print(response.body)


